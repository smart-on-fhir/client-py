# -*- coding: utf-8 -*-

import requests
import urllib
import logging
try:                                # Python 2.x
    import urlparse
except Exception as e:              # Python 3
    import urllib.parse as urlparse


class FHIRUnauthorizedException(Exception):
    """ Indicating a 401 response.
    """
    def __init__(self, response):
        self.response = response


class FHIRServer(object):
    """ Handles talking to a FHIR server.
    """
    
    def __init__(self, base_uri=None, state=None):
        self.auth = None
        self.base_uri = base_uri
        self._registration_uri = None
        self._authorize_uri = None
        self._token_uri = None
        self._metadata = None
        if state is not None:
            self.from_state(state)
    
    
    # MARK: Metadata
    
    @property
    def metadata(self):
        self.get_metadata()
        return self._metadata
    
    def get_metadata(self, if_needed=True):
        """ Returns the server's metadata, retrieving it if needed.
        """
        if self._metadata is None or not if_needed:
            logging.info('Fetching metadata')
            meta = self.request_json('metadata', nosign=True)
            try:
                extensions = meta['rest'][0]['security']['extension']
            except Exception as e:
                raise Exception("Invalid server metadata: {}\n{}".format(e, meta))
            
            # extract extensions from metadata: OAuth2 endpoint URIs
            for e in extensions:
                if e['url'] == "http://fhir-registry.smartplatforms.org/Profile/oauth-uris#register":
                    self._registration_uri = e['valueUri']
                elif e['url'] == "http://fhir-registry.smartplatforms.org/Profile/oauth-uris#authorize":
                    self._authorize_uri = e['valueUri']
                elif e['url'] == "http://fhir-registry.smartplatforms.org/Profile/oauth-uris#token":
                    self._token_uri = e['valueUri']

            self._metadata = meta
    
    
    # MARK: Authorization
    
    @property
    def authorize_uri(self):
        if self._authorize_uri is None:
            self.get_metadata()
        return self._authorize_uri
    
    @property
    def token_uri(self):
        if self._token_uri is None:
            self.get_metadata()
        return self._token_uri
    
    def did_authorize(self, auth):
        self.auth = auth
    
    
    # MARK: Requests
    
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
            'registration_uri': self._registration_uri,
            'authorize_uri': self._authorize_uri,
            'token_uri': self._token_uri,
            # 'metadata': self._metadata,       # don't save to state, not currently needed and it's BIG
        }
    
    def from_state(self, state):
        """ Update ivars from given state information.
        """
        assert state
        self.base_uri = state.get('base_uri') or self.base_uri
        self._registration_uri = state.get('registration_uri') or self._registration_uri
        self._authorize_uri = state.get('authorize_uri') or self._authorize_uri
        self._token_uri = state.get('token_uri') or self._token_uri
        self._metadata = state.get('metadata') or self._metadata
    
