# -*- coding: utf-8 -*-

import requests
import urllib
import logging
try:                                # Python 2.x
    import urlparse
    from urllib import urlencode
except Exception as e:              # Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


class FHIRServer(object):
    """ Handles talking to a FHIR server.
    """
    
    def __init__(self, base_uri=None, state=None):
        self.auth = None
        self.base_uri = base_uri
        self.registration_uri = None
        self.authorize_uri = None
        self._auth_url = None
        self.token_uri = None
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
            logging.info('Fetching metadata')
            meta = self.requestJSON('metadata', nosign=True)
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
            parts[3] = urlencode(params, doseq=True)
            self._auth_url = urlparse.urlunsplit(parts)
        return self._auth_url
    
    def exchange_code(self, params):
        """ Exchange the code received from the OAuth provider for an access
        token by POST-ing the given params (which must include the code).
        
        :returns: Decoded JSON response
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        req = requests.post(self.token_uri, data=params)
        req.raise_for_status()
        
        return req.json()
    
    def did_authorize(self, auth):
        self.auth = auth
    
    
    # MARK: Requests
    
    def requestJSON(self, path, nosign=False):
        """ Perform a request against the server's base with the given path.
        
        :param str path: The path to append to `base_uri`
        :param bool nosign: If set to True, the request will not be signed
        """
        assert self.base_uri and path
        url = urlparse.urljoin(self.base_uri, path)
        
        headers = {'Accept': 'application/json'}
        if not nosign and self.auth is not None and self.auth.can_sign_headers():
            headers = self.auth.signed_headers(headers)
        
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
            # 'metadata': self._metadata,       # don't save to state, not currently needed and it's BIG
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
        self._metadata = state.get('metadata') or self._metadata
    
