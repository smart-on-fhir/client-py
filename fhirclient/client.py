# -*- coding: utf-8 -*-

import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)

import requests
from server import FHIRServer, FHIRUnauthorizedException
from auth import FHIRAuth
import models.patient as patient

__version__ = '0.0.2'
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
        - `auth_type`: The authorization type, supports "oauth2". Defaults to "oauth2" if omitted
        - `redirect_uri`: The callback/redirect URL for your app, e.g. 'http://localhost:8000/fhir-app/' when testing locally
    """
    
    def __init__(self, settings=None, state=None):
        self.app_id = None
        self.server = None
        self.auth = None
        self.launch_context = None
        self._patient = None
        
        # init from state
        if state is not None:
            self.from_state(state)
        
        # init from settings dict
        elif settings is not None:
            self.app_id = settings['app_id']
            self.server = FHIRServer(base_uri=settings['api_base'])
            
            scope = scope_default
            if 'launch_token' in settings:
                scope = ' launch:'.join([scope, settings['launch_token']])
            else:
                scope = ' '.join([scope_nolaunch, scope])
            
            auth_type = settings.get('auth_type')
            redirect = settings.get('redirect_uri')
            self.auth = self._auth_for_type(auth_type, scope=scope, redirect_uri=redirect)
        else:
            raise Exception("Must either supply settings or a state upon client initialization")
    
    
    # MARK: Authorization
    
    @property
    def auth_type(self):
        return self.auth.auth_type if self.auth else None
    
    def _auth_for_type(self, auth_type, **kwargs):
        if auth_type is None:
            auth_type = 'oauth2'
        return FHIRAuth.create(auth_type, app_id=self.app_id, **kwargs)
    
    @property
    def ready(self):
        """ Returns True if the client is ready to make API calls (e.g. there
        is an access token).
        """
        return self.auth.ready if self.auth is not None else False
    
    @property
    def authorize_url(self):
        """ The URL to use to receive an authorization token.
        """
        return self.auth.authorize_url(self.server) if self.auth is not None else None
    
    def handle_callback(self, url):
        """ You can call this to have the client automatically handle the
        auth callback after the user has logged in.
        
        :param str url: The complete callback URL
        """
        self.launch_context = self.auth.handle_callback(url, self.server)
        self._set_authorized(True)
    
    def reauthorize(self):
        """ Try to reauthorize with the server; handled by our `auth` instance.
        
        :returns: A bool indicating reauthorization success
        """
        ctx = self.auth.reauthorize(self.server) if self.auth is not None else None
        if ctx is not None:
            self.launch_context = ctx
            return True
        return False
    
    
    def _set_authorized(self, flag):
        """ Internal method used to sync server and auth. """
        if flag:
            self.server.did_authorize(self.auth)
        else:
            self.server.did_authorize(None)
            self.auth.reset()
    
    
    # MARK: Current Patient
    
    @property
    def patient_id(self):
        return self.auth.patient_id
    
    @property
    def patient(self):
        if self._patient is None and self.ready:
            try:
                self._patient = patient.Patient.read(self.patient_id, self.server)
            except FHIRUnauthorizedException as e:
                if self.reauthorize():
                    self._patient = patient.Patient.read(self.patient_id, self.server)
                else:
                    self._set_authorized(False)
         
        return self._patient
    
    def human_name(self, human_name_instance):
        """ Formats a `HumanName` instance into a string.
        """
        if human_name_instance is None:
            return 'Unknown'
        
        parts = []
        for n in [human_name_instance.prefix, human_name_instance.given, human_name_instance.family, human_name_instance.suffix]:
            if n is not None:
                parts.extend(n)
        
        return ' '.join(parts) if len(parts) > 0 else 'Unnamed'
    
    def string_gender(self, gender_concept):
        """ Takes a `CodeableConcept` instance and returns either 'male',
        'female' or None.
        
        TODO: inspect coding system of the concepts and decide more thoroughly
        """
        if gender_concept is not None \
            and gender_concept.coding is not None \
            and len(gender_concept.coding) > 0:
            
            if gender_concept.coding[0].code: # and 'http://hl7.org/fhir/v3/AdministrativeGender' == gender_concept.coding[0].system:
                return 'male' if 'M' == gender_concept.coding[0].code else 'female'
        return None
    
    
    # MARK: State
    
    @property
    def state(self):
        return {
            'app_id': self.app_id,
            'server': self.server.state,
            'auth_type': self.auth_type,
            'auth': self.auth.state,
            'launch_context': self.launch_context,
        }
    
    def from_state(self, state):
        assert state
        self.app_id = state.get('app_id') or self.app_id
        self.launch_context = state.get('launch_context') or self.launch_context
        self.server = FHIRServer(state=state.get('server'))
        self.auth = self._auth_for_type(state.get('auth_type'), state=state.get('auth'))
        if self.auth is not None and self.auth.access_token is not None:
            self.server.did_authorize(self.auth)
    
