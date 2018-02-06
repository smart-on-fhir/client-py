# -*- coding: utf-8 -*-

import json
import requests
import urllib
import logging
try:                                # Python 2.x
    import urlparse
except ImportError as e:            # Python 3
    import urllib.parse as urlparse

from auth import FHIRAuth

FHIRJSONMimeType = 'application/fhir+json'

logger = logging.getLogger(__name__)


class FHIRUnauthorizedException(Exception):
    """ Indicating a 401 response.
    """
    def __init__(self, response):
        self.response = response


class FHIRPermissionDeniedException(Exception):
    """ Indicating a 403 response.
    """
    def __init__(self, response):
        self.response = response


class FHIRNotFoundException(Exception):
    """ Indicating a 404 response.
    """
    def __init__(self, response):
        self.response = response


class FHIRServer(object):
    """ Handles talking to a FHIR server.
    """
    
    def __init__(self, client, base_uri=None, state=None):
        self.client = client
        self.auth = None
        self.base_uri = None
        self.aud = None

        # Use a single requests Session for all "requests"
        self.session = requests.Session()
        
        # A URI can't possibly be less than 11 chars
        # make sure we end with "/", otherwise the last path component will be
        # lost when creating URLs with urllib
        if base_uri is not None and len(base_uri) > 10:
            self.base_uri = base_uri if '/' == base_uri[-1] else base_uri + '/'
            self.aud = base_uri
        self._capability = None
        if state is not None:
            self.from_state(state)
        if not self.base_uri or len(self.base_uri) <= 10:
            raise Exception("FHIRServer must be initialized with `base_uri` or `state` containing the base-URI, but neither happened")
    
    def should_save_state(self):
        if self.client is not None:
            self.client.save_state()
    
    
    # MARK: Server CapabilityStatement
    
    @property
    def capabilityStatement(self):
        self.get_capability()
        return self._capability
    
    def get_capability(self, force=False):
        """ Returns the server's CapabilityStatement, retrieving it if needed
        or forced.
        """
        if self._capability is None or force:
            logger.info('Fetching CapabilityStatement from {0}'.format(self.base_uri))
            from models import capabilitystatement
            conf = capabilitystatement.CapabilityStatement.read_from('metadata', self)
            self._capability = conf
            
            security = None
            try:
                security = conf.rest[0].security
            except Exception as e:
                logger.info("No REST security statement found in server capability statement")
            
            settings = {
                'aud': self.aud,
                'app_id': self.client.app_id if self.client is not None else None,
                'app_secret': self.client.app_secret if self.client is not None else None,
                'redirect_uri': self.client.redirect if self.client is not None else None,
            }
            self.auth = FHIRAuth.from_capability_security(security, settings)
            self.should_save_state()
    
    
    # MARK: Authorization
    
    @property
    def desired_scope(self):
        return self.client.desired_scope if self.client is not None else None
    
    @property
    def launch_token(self):
        return self.client.launch_token if self.client is not None else None
    
    @property
    def authorize_uri(self):
        if self.auth is None:
            self.get_capability()
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
        """ Check whether the server is ready to make calls, i.e. is has
        fetched its capability statement and its `auth` instance is ready.
        
        :returns: True if the server can make authenticated calls
        """
        return self.auth.ready if self.auth is not None else False
    
    def prepare(self):
        """ Check whether the server is ready to make calls, i.e. is has
        fetched its capability statement and its `auth` instance is ready.
        This method will fetch the capability statement if it hasn't already
        been fetched.
        
        :returns: True if the server can make authenticated calls
        """
        if self.auth is None:
            self.get_capability()
        return self.auth.ready if self.auth is not None else False
    
    def request_json(self, path, nosign=False):
        """ Perform a request for JSON data against the server's base with the
        given relative path.
        
        :param str path: The path to append to `base_uri`
        :param bool nosign: If set to True, the request will not be signed
        :throws: Exception on HTTP status >= 400
        :returns: Decoded JSON response
        """
        headers = {'Accept': 'application/json'}
        res = self._get(path, headers, nosign)
        
        return res.json()
    
    def request_data(self, path, headers={}, nosign=False):
        """ Perform a data request data against the server's base with the
        given relative path.
        """
        res = self._get(path, None, nosign)
        return res.content
    
    def _get(self, path, headers={}, nosign=False):
        """ Issues a GET request.
        
        :returns: The response object
        """
        assert self.base_uri and path
        url = urlparse.urljoin(self.base_uri, path)
        
        headers = {
            'Accept': FHIRJSONMimeType,
            'Accept-Charset': 'UTF-8',
        }
        if not nosign and self.auth is not None and self.auth.can_sign_headers():
            headers = self.auth.signed_headers(headers)
        
        # perform the request but intercept 401 responses, raising our own Exception
        res = self.session.get(url, headers=headers)
        self.raise_for_status(res)
        return res
    
    def put_json(self, path, resource_json, nosign=False):
        """ Performs a PUT request of the given JSON, which should represent a
        resource, to the given relative path.
        
        :param str path: The path to append to `base_uri`
        :param dict resource_json: The JSON representing the resource
        :param bool nosign: If set to True, the request will not be signed
        :throws: Exception on HTTP status >= 400
        :returns: The response object
        """
        url = urlparse.urljoin(self.base_uri, path)
        headers = {
            'Content-type': FHIRJSONMimeType,
            'Accept': FHIRJSONMimeType,
            'Accept-Charset': 'UTF-8',
        }
        if not nosign and self.auth is not None and self.auth.can_sign_headers():
            headers = self.auth.signed_headers(headers)
        
        # perform the request but intercept 401 responses, raising our own Exception
        res = self.session.put(url, headers=headers, data=json.dumps(resource_json))
        self.raise_for_status(res)
        return res
    
    def post_json(self, path, resource_json, nosign=False):
        """ Performs a POST of the given JSON, which should represent a
        resource, to the given relative path.
        
        :param str path: The path to append to `base_uri`
        :param dict resource_json: The JSON representing the resource
        :param bool nosign: If set to True, the request will not be signed
        :throws: Exception on HTTP status >= 400
        :returns: The response object
        """
        url = urlparse.urljoin(self.base_uri, path)
        headers = {
            'Content-type': FHIRJSONMimeType,
            'Accept': FHIRJSONMimeType,
            'Accept-Charset': 'UTF-8',
        }
        if not nosign and self.auth is not None and self.auth.can_sign_headers():
            headers = self.auth.signed_headers(headers)
        
        # perform the request but intercept 401 responses, raising our own Exception
        res = self.session.post(url, headers=headers, data=json.dumps(resource_json))
        self.raise_for_status(res)
        return res
    
    def post_as_form(self, url, formdata, auth=None):
        """ Performs a POST request with form-data, expecting to receive JSON.
        This method is used in the OAuth2 token exchange and thus doesn't
        request fhir+json.
        
        :throws: Exception on HTTP status >= 400
        :returns: The response object
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Accept': 'application/json',
        }
        res = self.session.post(url, data=formdata, auth=auth)
        self.raise_for_status(res)
        return res
    
    def delete_json(self, path, nosign=False):
        """ Issues a DELETE command against the given relative path, accepting
        a JSON response.
        
        :param str path: The relative URL path to issue a DELETE against
        :param bool nosign: If set to True, the request will not be signed
        :returns: The response object
        """
        url = urlparse.urljoin(self.base_uri, path)
        headers = {
            'Accept': FHIRJSONMimeType,
            'Accept-Charset': 'UTF-8',
        }
        if not nosign and self.auth is not None and self.auth.can_sign_headers():
            headers = self.auth.signed_headers(headers)
        
        # perform the request but intercept 401 responses, raising our own Exception
        res = self.session.delete(url)
        self.raise_for_status(res)
        return res
    
    def raise_for_status(self, response):
        if response.status_code < 400:
            return
        
        if 401 == response.status_code:
            raise FHIRUnauthorizedException(response)
        elif 403 == response.status_code:
            raise FHIRPermissionDeniedException(response)
        elif 404 == response.status_code:
            raise FHIRNotFoundException(response)
        else:
            response.raise_for_status()
    
    
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
    
