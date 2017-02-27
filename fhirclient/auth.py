# -*- coding: utf-8 -*-

import uuid
import logging
try:                                # Python 2.x
    import urlparse
    from urllib import urlencode
except Exception as e:              # Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

logger = logging.getLogger(__name__)

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
            raise Exception('Class {0} does not specify the auth_type it supports'.format(cls))
        if cls.auth_type not in FHIRAuth.auth_classes:
            FHIRAuth.auth_classes[cls.auth_type] = cls
        elif FHIRAuth.auth_classes[cls.auth_type] != cls:
            raise Exception('Class {0} is already registered for authorization type "{1}"'.format(FHIRAuth.auth_classes[cls.auth_type], cls.auth_type))
    
    @classmethod
    def from_capability_security(cls, security, state=None):
        """ Supply a capabilitystatement.rest.security statement and this
        method will figure out which type of security should be instantiated.
        
        :param security: A CapabilityStatementRestSecurity instance
        :param state: A settings/state dictionary
        :returns: A FHIRAuth instance or subclass thereof
        """
        auth_type = None
        
        # look for OAuth2 URLs in SMART security extensions
        if security is not None and security.extension is not None:
            for e in security.extension:
                if "http://fhir-registry.smarthealthit.org/StructureDefinition/oauth-uris" == e.url:
                    if e.extension is not None:
                        for ee in e.extension:
                            if 'token' == ee.url:
                                state['token_uri'] = ee.valueUri
                            elif 'authorize' == ee.url:
                                state['authorize_uri'] = ee.valueUri
                                auth_type = 'oauth2'
                            elif 'register' == ee.url:
                                state['registration_uri'] = ee.valueUri
                        break
                    else:
                        logger.warning("SMART AUTH: invalid `http://fhir-registry.smarthealthit.org/StructureDefinition/oauth-uris` extension: needs to include sub-extensions to define OAuth2 endpoints but there are none")
                
                # fallback to old extension URLs  
                elif "http://fhir-registry.smarthealthit.org/StructureDefinition/oauth-uris#register" == e.url:
                    state['registration_uri'] = e.valueUri
                elif "http://fhir-registry.smarthealthit.org/StructureDefinition/oauth-uris#authorize" == e.url:
                    state['authorize_uri'] = e.valueUri
                    auth_type = 'oauth2'
                elif "http://fhir-registry.smarthealthit.org/StructureDefinition/oauth-uris#token" == e.url:
                    state['token_uri'] = e.valueUri
        
        return cls.create(auth_type, state=state)
    
    @classmethod
    def create(cls, auth_type, state=None):
        """ Factory method to create the correct subclass for the given
        authorization type. """
        if not auth_type:
            auth_type = 'none'
        if auth_type in FHIRAuth.auth_classes:
            klass = FHIRAuth.auth_classes[auth_type]
            return klass(state=state)
        raise Exception('No class registered for authorization type "{0}"'.format(auth_type))
    
    
    def __init__(self, state=None):
        self.app_id = None
        if state is not None:
            self.from_state(state)
    
    @property
    def ready(self):
        """ Indicates whether the authorization part is ready to make
        resource requests. """
        return True
    
    def reset(self):
        pass
    
    def can_sign_headers(self):
        return False
    
    def authorize_uri(self, server):
        """ Return the authorize URL to use, if any. """
        return None
    
    def handle_callback(self, url, server):
        """ Return the launch context. """
        raise Exception("{0} cannot handle callback URL".format(self))
    
    def reauthorize(self):
        """ Perform a re-authorization of some form.
        
        :returns: The launch context dictionary or None on failure
        """
        return None
    
    
    # MARK: State
    
    @property
    def state(self):
        return {
            'app_id': self.app_id,
        }
    
    def from_state(self, state):
        """ Update ivars from given state information.
        """
        assert state
        self.app_id = state.get('app_id') or self.app_id


class FHIROAuth2Auth(FHIRAuth):
    """ OAuth2 handling class for FHIR servers.
    """
    auth_type = 'oauth2'
    
    def __init__(self, state=None):
        self.aud = None
        self._registration_uri = None
        self._authorize_uri = None
        self._redirect_uri = None
        self._token_uri = None
        
        self.auth_state = None
        self.app_secret = None
        self.access_token = None
        self.refresh_token = None
        
        super(FHIROAuth2Auth, self).__init__(state=state)
    
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
        headers['Authorization'] = "Bearer {0}".format(self.access_token)
        
        return headers
    
    
    # MARK: OAuth2 Flow
    
    def authorize_uri(self, server):
        """ The URL to authorize against. The `server` param is supplied so
        that the server can be informed of state changes that need to be
        stored.
        """
        auth_params = self._authorize_params(server)
        logger.debug("SMART AUTH: Will use parameters for `authorize_uri`: {0}".format(auth_params))
        
        # the authorize uri may have params, make sure to not lose them
        parts = list(urlparse.urlsplit(self._authorize_uri))
        if len(parts[3]) > 0:
            args = urlparse.parse_qs(parts[3])
            args.update(auth_params)
            auth_params = args
        parts[3] = urlencode(auth_params, doseq=True)
        
        return urlparse.urlunsplit(parts)
    
    def _authorize_params(self, server):
        """ The URL parameters to use when requesting a token code.
        """
        if server is None:
            raise Exception("Cannot create an authorize-uri without server instance")
        if self.auth_state is None:
            self.auth_state = str(uuid.uuid4())[:8]
            server.should_save_state()
        
        params = {
            'response_type': 'code',
            'client_id': self.app_id,
            'redirect_uri': self._redirect_uri,
            'scope': server.desired_scope,
            'aud': self.aud,
            'state': self.auth_state,
        }
        if server.launch_token is not None:
            params['launch'] = server.launch_token
        return params
    
    def handle_callback(self, url, server):
        """ Verify OAuth2 callback URL and exchange the code, if everything
        goes well, for an access token.
        
        :param str url: The callback/redirect URL to handle
        :param server: The Server instance to use
        :returns: The launch context dictionary
        """
        logger.debug("SMART AUTH: Handling callback URL")
        if url is None:
            raise Exception("No callback URL received")
        try:
            args = dict(urlparse.parse_qsl(urlparse.urlsplit(url)[3]))
        except Exception as e:
            raise Exception("Invalid callback URL: {0}".format(e))
        
        # verify response
        err = self.extract_oauth_error(args)
        if err is not None:
            raise Exception(err)
        
        stt = args.get('state')
        if stt is None or self.auth_state != stt:
            raise Exception("Invalid state, will not use this code. Have: {0}, want: {1}".format(stt, self.auth_state))
        
        code = args.get('code')
        if code is None:
            raise Exception("Did not receive a code, only have: {0}".format(', '.join(args.keys())))
        
        # exchange code for token
        exchange = self._code_exchange_params(code)
        return self._request_access_token(server, exchange)
    
    def _code_exchange_params(self, code):
        """ These parameters are used by to exchange the given code for an
        access token.
        """
        return {
            'client_id': self.app_id,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': self._redirect_uri,
            'state': self.auth_state,
        }
    
    def _request_access_token(self, server, params):
        """ Requests an access token from the instance's server via a form POST
        request, remembers the token (and patient id if there is one) or
        raises an Exception.
        
        :returns: A dictionary with launch params
        """
        if server is None:
            raise Exception("I need a server to request an access token")
        
        logger.debug("SMART AUTH: Requesting access token from {0}".format(self._token_uri))
        auth = None
        if self.app_secret:
            auth = (self.app_id, self.app_secret)
        ret_params = server.post_as_form(self._token_uri, params, auth).json()
        
        self.access_token = ret_params.get('access_token')
        if self.access_token is None:
            raise Exception("No access token received")
        del ret_params['access_token']
        
        if 'expires_in' in ret_params:
            del ret_params['expires_in']
        
        # The refresh token issued by the authorization server. If present, the
        # app should discard any previous refresh_token associated with this
        # launch, replacing it with this new value.
        refresh_token = ret_params.get('refresh_token')
        if refresh_token is not None:
            self.refresh_token = refresh_token
            del ret_params['refresh_token']
        
        logger.debug("SMART AUTH: Received access token: {0}, refresh token: {1}"
            .format(self.access_token is not None, self.refresh_token is not None))
        return ret_params
    
    
    # MARK: Reauthorization
    
    def reauthorize(self, server):
        """ Perform reauthorization.
        
        :param server: The Server instance to use
        :returns: The launch context dictionary, or None on failure
        """
        if self.refresh_token is None:
            logger.debug("SMART AUTH: Cannot reauthorize without refresh token")
            return None
        
        logger.debug("SMART AUTH: Refreshing token")
        reauth = self._reauthorize_params()
        return self._request_access_token(server, reauth)
    
    def _reauthorize_params(self):
        """ Parameters to be used in a reauthorize request.
        """
        if self.refresh_token is None:
            raise Exception("Cannot produce reauthorize parameters without refresh token")
        return {
            'client_id': self.app_id,
            #'client_secret': None,             # we don't use it
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
        }
    
    
    # MARK: State
    
    @property
    def state(self):
        s = super(FHIROAuth2Auth, self).state
        s['aud'] = self.aud
        s['registration_uri'] = self._registration_uri
        s['authorize_uri'] = self._authorize_uri
        s['redirect_uri'] = self._redirect_uri
        s['token_uri'] = self._token_uri
        if self.auth_state is not None:
            s['auth_state'] = self.auth_state
        if self.app_secret is not None:
            s['app_secret'] = self.app_secret
        if self.access_token is not None:
            s['access_token'] = self.access_token
        if self.refresh_token is not None:
            s['refresh_token'] = self.refresh_token
        
        return s
    
    def from_state(self, state):
        """ Update ivars from given state information.
        """
        super(FHIROAuth2Auth, self).from_state(state)
        self.aud = state.get('aud') or self.aud
        self._registration_uri = state.get('registration_uri') or self._registration_uri
        self._authorize_uri = state.get('authorize_uri') or self._authorize_uri
        self._redirect_uri = state.get('redirect_uri') or self._redirect_uri
        self._token_uri = state.get('token_uri') or self._token_uri
        self.auth_state = state.get('auth_state') or self.auth_state
        self.app_secret = state.get('app_secret') or self.app_secret
        
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
            return "Authorization error: {0}.".format(err_code)
        
        return None
    

# register classes
FHIRAuth.register()
FHIROAuth2Auth.register()
