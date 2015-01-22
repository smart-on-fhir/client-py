# -*- coding: utf-8 -*-

import requests
import urllib
import logging
try:                                # Python 2.x
    import urlparse
except Exception as e:              # Python 3
    import urllib.parse as urlparse

from auth import FHIRAuth
from models import conformance


class FHIRUnauthorizedException(Exception):
    """ Indicating a 401 response.
    """
    def __init__(self, response):
        self.response = response


class FHIRServer(object):
    """ Handles talking to a FHIR server.
    """
    
    def __init__(self, client, base_uri=None, state=None):
        self.client = client
        self.auth = None
        self.base_uri = base_uri
        self._conformance = None
        if state is not None:
            self.from_state(state)
    
    def should_save_state(self):
        if self.client is not None:
            self.client.save_state()
    
    
    # MARK: Server Conformance Statement
    
    @property
    def conformance(self):
        self.get_conformance()
        return self._conformance
    
    def get_conformance(self, force=False):
        """ Returns the server's conformance statement, retrieving it if needed
        or forced.
        """
        if self._conformance is None or force:
            logging.info('Fetching conformance statement from {}'.format(self.base_uri))
            conf = conformance.Conformance.read_from('metadata', self)
            self._conformance = conf
            
            security = None
            try:
                security = conf.rest[0].security
            except Exception as e:
                logging.info("No REST security statement found in server conformance statement")
            
            settings = {
                'app_id': self.client.app_id if self.client is not None else None,
                'scope': self.client.scope if self.client is not None else None,
                'redirect_uri': self.client.redirect if self.client is not None else None,
            }
            self.auth = FHIRAuth.from_conformance_security(security, settings)
            self.should_save_state()
    
    
    # MARK: Authorization
    
    @property
    def authorize_uri(self):
        if self.auth is None:
            self.get_conformance()
        return self.auth.authorize_uri(self)
    
    def handle_callback(self, url):
        if self.auth is None:
            raise Exception("Not ready to handle callback, I do not have an auth instance")
        return self.auth.handle_callback(url, self)
    
    def reauthorize(self):
        if self.auth is None:
            raise Exception("Not ready to reauthorize, I do not have an auth instance")
        return self.auth.reauthorize(self) if self.auth is not None else None
    
    
    # MARK: Requests
    
    @property
    def ready(self):
        return self.auth.ready if self.auth is not None else False
    
    def request_json(self, path, nosign=False):
        """ Perform a request against the server's base with the given path.
        
        :param str path: The path to append to `base_uri`
        :param bool nosign: If set to True, the request will not be signed
        """
        assert self.base_uri and path
        url = urlparse.urljoin(self.base_uri, path)
        
        headers = {'Accept': 'application/json'}
        if not nosign and self.auth is not None and self.auth.can_sign_headers():
            headers = self.auth.signed_headers(headers)
        
        # perform the request but intercept 401 responses, raising our own Exception
        res = requests.get(url, headers=headers)
        if 401 == res.status_code:
            raise FHIRUnauthorizedException(res)
        else:
            res.raise_for_status()
        
        return res.json()
    
    def post_as_form(self, url, formdata):
        """ Performs a POST request with form-data, expecting to receive JSON.
        
        :returns: Decoded JSON response
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Accept': 'application/json',
        }
        req = requests.post(url, data=formdata)
        req.raise_for_status()
        
        return req.json()
    
    
    # MARK: State Handling
    
    @property
    def state(self):
        """ Return current state.
        """
        return {
            'base_uri': self.base_uri,
            'auth_type': self.auth.auth_type if self.auth is not None else 'none',
            'auth': self.auth.state if self.auth is not None else None,
        }
    
    def from_state(self, state):
        """ Update ivars from given state information.
        """
        assert state
        self.base_uri = state.get('base_uri') or self.base_uri
        self.auth = FHIRAuth.create(state.get('auth_type'), state=state.get('auth'))
    
