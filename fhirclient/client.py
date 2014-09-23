# -*- coding: utf-8 -*-
#
#   TO DO
#    [ ] dynamic handlers for the various FHIR REST call variants and arguments (a la JS client)
#    [ ] add in Pascal's parser for FHIR profiles
#    [ ] ability to dynamically register the app if not present in the auth server
#    [ ] exception handlers and assert unit testing
#    [ ] documentation and tutorial

import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import requests
from server import FHIRServer
from auth import FHIRAuth
from models.Patient import Patient

__version__ = '0.0.1'
__author__ = 'SMART Platforms Team'
__license__ = 'APACHE2'
__copyright__ = "Copyright 2014 Boston Children's Hospital"

scope_default = 'user/*.* patient/*.read openid profile'
scope_nolaunch = 'launch/patient'


class FHIRClient(object):
    """ Instances of this class handle authorizing and talking to SMART on FHIR
    servers.
    
    The settings dictionary supports:
    
        - `app_id`: Your app/client-id, e.g. 'my_web_app'
        - `api_base`: The SMART service to connect to, e.g. 'https://fhir-api.smartplatforms.org'
        - `redirect_uri`: The callback/redirect URL for your app, e.g. 'http://localhost:8000/fhir-app/' when testing locally
    """
    
    def __init__(self, settings=None, state=None):
        self.app_id = None
        self.server = None
        self.auth = None
        self._patient = None
        
        # init from state
        if state is not None:
            self.from_state(state)
        
        # init from settings dict
        elif settings is not None:
            try:
                self.app_id = settings['app_id']
                self.server = FHIRServer(base_uri=settings['api_base'])
                
                scope = scope_default
                if 'launch_token' in settings:
                    scope = ' launch:'.join([scope, settings['launch_token']])
                else:
                    scope = ' '.join([scope_nolaunch, scope])
                self.auth = FHIRAuth(app_id=self.app_id, scope=scope, redirect_uri=settings['redirect_uri'])
            
            except Exception as e:
                raise Exception("Incomplete initialization, need all of these: app_id, redirect_uri and api_base, have: {}  Error was: {}".format(settings.keys(), e))
        else:
            raise Exception("Must either supply settings or a state upon client initialization")
    
    
    # MARK: Authorization
    
    @property
    def ready(self):
        """ Returns True if the client is ready to make API calls (i.e. there
        is an access token).
        """
        return True if self.auth.access_token is not None else False
    
    @property
    def authorize_url(self):
        """ The URL to use to receive an authorization token.
        """
        auth_params = self.auth.authorize_params()
        return self.server.authorize_url(auth_params)
    
    def handle_callback(self, url):
        """ You can call this to have the client automatically handle the
        callback after the user has logged in.
        
        :param str url: The complete callback URL
        """
        code = self.auth.handle_callback(url)
        req_body = self.auth.code_exchange_params(code)
        ret_params = self.server.exchange_code(req_body)
        self.auth.handle_code_exchange(ret_params)
        self.server.did_authorize(self.auth)
    
    
    # MARK: Current Patient
    
    @property
    def patient_id(self):
        return self.auth.patient_id
    
    @property
    def patient(self):
        if self._patient is None:
            ret = Patient.read(self.patient_id, self.server)
            self._patient = Patient(jsondict=ret)
        return self._patient
    
    
    # MARK: State
    
    @property
    def state(self):
        return {
            'app_id': self.app_id,
            'server': self.server.state,
            'auth': self.auth.state,
        }
    
    def from_state(self, state):
        assert state
        self.app_id = state.get('app_id') or self.app_id
        self.server = FHIRServer(state=state.get('server'))
        self.auth = FHIRAuth(self.app_id, state=state.get('auth'))
        if self.auth.access_token is not None:
            self.server.did_authorize(self.auth)
    
