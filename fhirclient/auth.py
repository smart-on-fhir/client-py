# -*- coding: utf-8 -*-

import uuid
import logging
try:                                # Python 2.x
    import urlparse
    from urllib import urlencode
except Exception as e:              # Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


class FHIRAuth(object):
    """ Superclass to handle authorization flow and state.
    """
    auth_type = 'none'
    auth_classes = {}
    
    @classmethod
    def register(cls):
        """ Register this class to handle authorization types of the given
        type. """
        if not cls.auth_type:
            raise Exception('Class {} does not specify the auth_type it supports'.format(cls))
        if cls.auth_type not in FHIRAuth.auth_classes:
            FHIRAuth.auth_classes[cls.auth_type] = cls
        elif FHIRAuth.auth_classes[cls.auth_type] != cls:
            raise Exception('Class {} is already registered for authorization type "{}"'.format(FHIRAuth.auth_classes[cls.auth_type], cls.auth_type))
    
    @classmethod
    def create(cls, auth_type, app_id, **kwargs):
        """ Factory method to create the correct subclass for the given
        authorization type. """
        if not auth_type:
            auth_type = 'none'
        if auth_type in FHIRAuth.auth_classes:
            klass = FHIRAuth.auth_classes[auth_type]
            return klass(app_id=app_id, **kwargs)
        raise Exception('No class registered for authorization type "{}"'.format(auth_type))
    
    def __init__(self, app_id, state=None, patient_id=None):
        self.app_id = app_id
        
        self.patient_id = patient_id
        """ The currently active patient. """
        
        if state is not None:
            self.from_state(state)
    
    @property
    def ready(self):
        """ Indicates whether the authorization part is ready to make
        resource requests. """
        return True
    
    def reset(self):
        self.patient_id = None
    
    def can_sign_headers(self):
        return False
    
    def authorize_url(self, server):
        """ Return the authorize URL to use against the given server. The
        server must have a `metadata` dict property. """
        return None
    
    def handle_callback(self, url, server):
        """ Return the launch context. """
        raise Exception("{} cannot handle callback URL".format(self))
    
    def reauthorize(self, server):
        """ Perform a re-authorization of some form.
        
        :returns: The launch context dictionary or None on failure
        """
        return None
    
    
    # MARK: State
    
    @property
    def state(self):
        return {
            'patient_id': self.patient_id,
        }
    
    def from_state(self, state):
        """ Update ivars from given state information.
        """
        assert state
        self.patient_id = state.get('patient_id') or self.patient_id

    
class FHIROAuth2Auth(FHIRAuth):
    """ OAuth2 handling class for FHIR servers.
    """
    auth_type = 'oauth2'
    
    def __init__(self, app_id, scope=None, redirect_uri=None, state=None):
        self.scope = scope
        self.redirect_uri = redirect_uri
        
        self.auth_state = None
        self.access_token = None
        self.refresh_token = None
        
        super(FHIROAuth2Auth, self).__init__(app_id, state=state)
    
    @property
    def ready(self):
        return True if self.access_token else False
    
    def reset(self):
        super(FHIROAuth2Auth, self).reset()
        self.access_token = None
        self.auth_state = None
    
    
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
    
    def authorize_url(self, server):
        auth_params = self.authorize_params()
        
        # the authorize uri may have params, make sure to not lose them
        parts = list(urlparse.urlsplit(server.authorize_uri))
        if len(parts[3]) > 0:
            args = urlparse.parse_qs(parts[3])
            args.update(auth_params)
            auth_params = args
        parts[3] = urlencode(auth_params, doseq=True)
        
        return urlparse.urlunsplit(parts)
    
    def authorize_params(self):
        """ The URL parameters to use when requesting a token code.
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
    
    def handle_callback(self, url, server):
        """ Verify OAuth2 callback URL and exchange the code, if everything
        goes well, for an access token.
        
        :param str url: The callback/redirect URL to handle
        :param server: The FHIR server to handle the callback against
        :returns: The launch context dictionary
        """
        logging.debug("Handling callback URL")
        if url is None:
            raise Exception("No callback URL received")
        if server is None:
            raise Exception("I need a server against which to handle the callback")
        try:
            args = dict(urlparse.parse_qsl(urlparse.urlsplit(url)[3]))
        except Exception as e:
            raise Exception("Invalid callback URL: {}".format(e))
        
        # verify response
        err = self.extract_oauth_error(args)
        if err is not None:
            raise Exception(err)
        
        stt = args.get('state')
        if stt is None or self.auth_state != stt:
            raise Exception("Invalid state, will not use this code. Have: {}, want: {}".format(stt, self.auth_state))
        
        code = args.get('code')
        if code is None:
            raise Exception("Did not receive a code, only have: {}".format(', '.join(args.keys())))
        
        # exchange code for token
        exchange = self.code_exchange_params(code)
        return self.request_access_token(server, exchange)
    
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
            # 'scope': self.scope,          # don't use, will return 400 when using launch:xxx scope
        }
    
    def request_access_token(self, server, params):
        """ Requests an access token from the given server via a form POST
        request, remembers the token (and patient id if there is one) or
        raises an Exception.
        
        :returns: A dictionary with launch params
        """
        logging.debug("Requesting access token from {}".format(server.token_uri))
        ret_params = server.post_as_form(server.token_uri, params)
        
        self.access_token = ret_params.get('access_token')
        if self.access_token is None:
            raise Exception("No access token received")
        del ret_params['access_token']
        if 'expires_in' in ret_params:
            del ret_params['expires_in']
        
        self.refresh_token = ret_params.get('refresh_token')
        if self.refresh_token is not None:
            del ret_params['refresh_token']
        
        if 'patient' in ret_params:
            self.patient_id = ret_params['patient']
        
        return ret_params
    
    
    # MARK: Reauthorization
    
    def reauthorize(self, server):
        """ Perform reauthorization.
        
        :returns: The launch context dictionary, or None on failure
        """
        if self.refresh_token is None:
            return None
        
        reauth = self.reauthorize_params()
        return self.request_access_token(server, reauth)
    
    def reauthorize_params(self):
        """ Parameters to be used in a reauthorize request.
        """
        if self.refresh_token is None:
            raise Exception("Cannot produce reauthorize parameters without refresh token")
        return {
            'client_id': self.app_id,
            #'client_secret': None,             # we don't use it
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
            #'scope': self.scope,               # not needed, cannot be changed anyway
        }
    
    
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
        super(FHIROAuth2Auth, self).from_state(state)
        self.scope = state.get('scope') or self.scope
        self.redirect_uri = state.get('redirect_uri') or self.redirect_uri
        self.auth_state = state.get('auth_state') or self.auth_state
        
        self.access_token = state.get('access_token') or self.access_token
        self.refresh_token = state.get('refresh_token') or self.refresh_token
    

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
    

# register classes
FHIRAuth.register()
FHIROAuth2Auth.register()
