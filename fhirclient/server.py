# -*- coding: utf-8 -*-

import requests
import urllib
import urlparse


class FHIRServer(object):
    """ Handles talking to a FHIR server.
    """
    
    def __init__(self, base_uri=None, state=None):
        self.base_uri = base_uri
        self.registration_uri = None
        self.authorize_uri = None
        self._auth_url = None
        self.token_uri = None
        self.access_token = None
        self.refresh_token = None
        self.patient_id = None
        """ The currently active patient. """
        
        self._metadata = None
        if state is not None:
            self.from_state(state)
    
    
    # MARK: Metadata
    
    @property
    def metadata(self):
        self.getMetadataIfNeeded()
        return self._metadata
    
    def getMetadataIfNeeded(self):
        """ Returns the server's metadata, retrieving it if necessary.
        """
        if self._metadata is None:
            meta = self.requestJSON('metadata')
            try:
                extensions = meta['rest'][0]['security']['extension']
            except Exception as e:
                raise Exception("Invalid server metadata: {}\n{}".format(e, meta))
            
            # extract extensions from metadata: OAuth2 endpoint URIs
            for e in extensions:
                if e['url'] == "http://fhir-registry.smartplatforms.org/Profile/oauth-uris#register":
                    self.registration_uri = e['valueUri']
                elif e['url'] == "http://fhir-registry.smartplatforms.org/Profile/oauth-uris#authorize":
                    self.authorize_uri = e['valueUri']
                elif e['url'] == "http://fhir-registry.smartplatforms.org/Profile/oauth-uris#token":
                    self.token_uri = e['valueUri']

            self._metadata = meta
    
    
    # MARK: Authorization
    
    def authorize_url(self, params):
        if self._auth_url is None:
            self.getMetadataIfNeeded()
            
            # the authorize uri may have params, make sure to not lose them
            parts = list(urlparse.urlsplit(self.authorize_uri))
            if len(parts[3]) > 0:
                args = urlparse.parse_qs(parts[3])
                args.update(params)
                params = args
            parts[3] = urllib.urlencode(params, doseq=True)
            self._auth_url = urlparse.urlunsplit(parts)
        return self._auth_url
    
    def handle_callback(self, url):
        """ Handle OAuth2 callback URL.
        """
        if url is None:
            raise Exception("No callback URL received")
        try:
            args = urlparse.parse_qs(urlparse.urlsplit(url)[3])
        except Exception as e:
            raise Exception("Invalid callback URL: {}".format(e))
        
        err = self.extract_oauth_error(args)
        if err is not None:
            raise Exception(err)
        
        print("All good", args)
    
    def extract_oauth_error(self, args):
        """ Check if an argument dictionary contains OAuth error information.
        """
        # "error_description" is optional, we prefer it if it's present
        if 'error_description' in args:
            return args['error_description'][0].replace('+', ' ')
        
        # the "error" response is required if there are errors, look for it
        if 'error' in args:
            err_code = args['error'][0]
            if 'invalid_request' == err_code:
                return "The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed."
            if 'unauthorized_client' == err_code:
                return "The client is not authorized to request an access token using this method."
            if 'access_denied' == err_code:
                return "The resource owner or authorization server denied the request."
            if 'unsupported_response_type' == err_code:
                return "The authorization server does not support obtaining an access token using this method."
            if 'invalid_scope' == err_code:
                return "The requested scope is invalid, unknown, or malformed."
            if 'server_error' == err_code:
                return "The authorization server encountered an unexpected condition that prevented it from fulfilling the request."
            if 'temporarily_unavailable' == err_code:
                return "The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
            return "Authorization error: {}.".format(err_code)
        
        return None
    
    
    # MARK: Requests
    
    def requestJSON(self, path, auth=None):
        """ Perform a request against the server's base with the given path.
        
        :param str path: The path to append to `base_uri`
        :param auth: The authorization to use
        """
        assert self.base_uri and path
        url = urlparse.urljoin(self.base_uri, path)
        headers = {'Accept': 'application/json'}
        # TODO: sign if `auth` is not None
        req = requests.get(url, headers=headers)
        req.raise_for_status()
        
        return req.json()
    
    
    # MARK: State Handling
    
    @property
    def state(self):
        """ Return current state.
        """
        return {
            'base_uri': self.base_uri,
            'registration_uri': self.registration_uri,
            'authorize_uri': self.authorize_uri,
            'auth_url': self._auth_url,
            'token_uri': self.token_uri,
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'patient_id': self.patient_id,
            'metadata': self._metadata,
        }
    
    def from_state(self, state):
        """ Update ivars from given state information.
        """
        assert state
        self.base_uri = state.get('base_uri') or self.base_uri
        self.registration_uri = state.get('registration_uri') or self.registration_uri
        self.authorize_uri = state.get('authorize_uri') or self.authorize_uri
        self._auth_url = state.get('auth_url') or self._auth_url
        self.token_uri = state.get('token_uri') or self.token_uri
        self.access_token = state.get('access_token') or self.access_token
        self.refresh_token = state.get('refresh_token') or self.refresh_token
        self.patient_id = state.get('patient_id') or self.patient_id
        self._metadata = state.get('metadata') or self._metadata
    
