#   TO DO
#    [ ] dynamic handlers for the various FHIR REST call variants and arguments (a la JS client)
#    [ ] add in Pascal's parser for FHIR profiles
#    [ ] ability to dynamically register the app if not present in the auth server
#    [ ] exception handlers and assert unit testing
#    [ ] documentation and tutorial

import requests
from server import FHIRServer

__version__ = '0.0.1'
__author__ = 'SMART Platforms Team'
__license__ = 'APACHE2'
__copyright__ = "Copyright 2014 Boston Children's Hospital"


class FHIRClient(object):
    """ Instances of this class handle authorizing and talking to SMART on FHIR
    servers.
    """
    
    def __init__(self, settings=None, state=None):
        self.app_id = None
        self.redirect = None
        self.scope = None
        self.server = None
        
        # init from state
        if state is not None:
            self.from_state(state)
        
        # init from settings dict
        elif settings is None:
            raise Exception("Must either supply settings or a state upon client initialization")
        else:
            try:
                self.app_id = settings['app_id']
                self.redirect = settings['redirect']
                self.server = FHIRServer(base_uri=settings['api_base'])
                
                self.scope = settings['scope']
                if 'launch_token' in settings:
                    self.scope += ' launch:{}'.format(settings['launch_token'])
            
            except Exception as e:
                raise Exception("Incomplete initialization, need all of these: app_id, redirect, api_base and scope: {}".format(e))
        
    
    
    # MARK: Authorization
    
    @property
    def authorize_url(self):
        """ The URL to use to receive an authorization token. """
        return self.server.authorize_url({
            'client_id': self.app_id,
            'response_type': 'code',
            'scope': self.scope,
            'redirect_url': self.redirect,
        })
    
    def handle_callback(self, url):
        """ You can call this to have the client automatically handle the
        callback after the user has logged in.
        
        :param str url: The complete callback URL
        """
        self.server.handle_callback(url)
    
    
    # MARK: State
    
    @property
    def state(self):
        return {
            'app_id': self.app_id,
            'redirect': self.redirect,
            'scope': self.scope,
            'provider': self.server.state,
        }
    
    def from_state(self, state):
        assert state
        self.app_id = state.get('app_id') or self.app_id
        self.redirect = state.get('redirect') or self.redirect
        self.scope = state.get('scope') or self.scope
        self.server = FHIRServer(state=state.get('provider'))
    
    @property
    def patient_id(self):
        return self.server.patient_id
    
    
    def update_access_token (self, authorization_code):
        c = self._settings['client']
        p = self._settings['provider']
        url = p['oauth2']['token_uri']
        auth = (c['app_id'], self._secret)
        params = {
          'code': authorization_code,
          'grant_type': 'authorization_code',
          'redirect_uri': c['redirect'],
          'client_id': c['app_id']
        }
        
        r = requests.get(url, params=params, auth=auth)
        res = r.json()

        p['access_token_type'] = res['token_type']
        p['access_token'] = res['access_token']
        p['pid'] = res['patient']

    # TO DO: generate this convenience method on the fly
    def Patient (self):
        p = self._settings['provider']
        url = p['api_base'] + "/Patient/" + self.patient_id

        # TODO: There may be a better way to specify non-basic authorization header in requests
        headers = {
            'Authorization': ' '.join((p['access_token_type'], p['access_token'])),
            'Accept': 'application/json'
        }

        r = requests.get(url, headers=headers)
        return r.json()
       
    def get(self, type):
        p = self._settings['provider']
        url = p['api_base'] + "/" + type + "/_search?patient:Patient=" + p['pid']

        # TODO: There may be a better way to specify non-basic authorization header in requests
        headers = {
            'Authorization': ' '.join((p['access_token_type'], p['access_token'])),
            'Accept': 'application/json'
        }

        r = requests.get(url, headers=headers)
        dt = r.json()
        res = []
        try:
            for e in dt['entry']:
                res.append(e['content'])
        except:
            pass
        return res
