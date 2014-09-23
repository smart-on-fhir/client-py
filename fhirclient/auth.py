# -*- coding: utf-8 -*-

import uuid
try:                                # Python 2.x
    import urlparse
except Exception as e:              # Python 3
    import urllib.parse as urlparse


class FHIRAuth(object):
    """ Handles authorization flow and state, written for OAuth2 code flows.
    """
    
    def __init__(self, app_id, scope=None, redirect_uri=None, state=None):
        self.app_id = app_id
        self.scope = scope
        self.redirect_uri = redirect_uri
        
        self.patient_id = None
        """ The currently active patient. """
        
        self.auth_state = None
        self.access_token = None
        self.refresh_token = None
        
        if state is not None:
            self.from_state(state)
    
    
    # MARK: Signing/Authorizing Request Headers
    
    def can_sign_headers(self):
        return True if self.access_token is not None else False
    
    def signed_headers(self, headers):
        """ Returns updated HTTP request headers, if possible, raises if there
        is no access_token.
        """
        if not self.can_sign_headers():
            raise Exception("Cannot sign headers since I have no access token")
        
        if headers is None:
            headers = {}
        headers['Authorization'] = "Bearer {}".format(self.access_token)
        
        return headers
    
    
    # MARK: OAuth2 Flow
    
    def authorize_params(self):
        """ The URL parameters to use when reuqesting a token code.
        """
        if self.auth_state is None:
            self.auth_state = str(uuid.uuid4())[:8]
        
        return {
            'client_id': self.app_id,
            'response_type': 'code',
            'scope': self.scope,
            'state': self.auth_state,
            'redirect_uri': self.redirect_uri,
        }
    
    def handle_callback(self, url):
        """ Verify OAuth2 callback URL and exchange the code, if everything
        goes well, for an access token.
        
        :param str url: The callback/redirect URL to handle
        :returns: The code that can be exchanged for an access token
        """
        if url is None:
            raise Exception("No callback URL received")
        try:
            args = dict(urlparse.parse_qsl(urlparse.urlsplit(url)[3]))
        except Exception as e:
            raise Exception("Invalid callback URL: {}".format(e))
        
        err = self.extract_oauth_error(args)
        if err is not None:
            raise Exception(err)
        
        stt = args.get('state')
        if stt is None or self.auth_state != stt:
            raise Exception("Invalid state, will not use this code. Have: {}, want: {}".format(stt, self.auth_state))
        
        code = args.get('code')
        if code is None:
            raise Exception("Did not receive a code, only have: {}".format(', '.join(args.keys())))
        
        return code
    
    def code_exchange_params(self, code):
        """ These parameters are used by the server to exchange the given code
        for an access token.
        """
        return {
            'client_id': self.app_id,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri,
            'state': self.auth_state,
            'scope': self.scope,
        }
    
    def handle_code_exchange(self, params):
        """ Handles the response from a token exchange call.
        """
        self.access_token = params.get('access_token')
        if self.access_token is None:
            raise Exception("No access token received")
        self.patient_id = params.get('patient')
    
    
    # MARK: State
    
    @property
    def state(self):
        return {
            'scope': self.scope,
            'redirect_uri': self.redirect_uri,
            'auth_state': self.auth_state,
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'patient_id': self.patient_id,
        }
    
    def from_state(self, state):
        """ Update ivars from given state information.
        """
        assert state
        self.scope = state.get('scope') or self.scope
        self.redirect_uri = state.get('redirect_uri') or self.redirect_uri
        self.auth_state = state.get('auth_state') or self.auth_state
        
        self.access_token = state.get('access_token') or self.access_token
        self.refresh_token = state.get('refresh_token') or self.refresh_token
        self.patient_id = state.get('patient_id') or self.patient_id
    

    # MARK: Utilities    
    
    def extract_oauth_error(self, args):
        """ Check if an argument dictionary contains OAuth error information.
        """
        # "error_description" is optional, we prefer it if it's present
        if 'error_description' in args:
            return args['error_description'].replace('+', ' ')
        
        # the "error" response is required if there are errors, look for it
        if 'error' in args:
            err_code = args['error']
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
    
