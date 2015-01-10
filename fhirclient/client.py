# -*- coding: utf-8 -*-

import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)

from server import FHIRServer, FHIRUnauthorizedException
import models.patient as patient

__version__ = '0.0.4'
__author__ = 'SMART Platforms Team'
__license__ = 'APACHE2'
__copyright__ = "Copyright 2015 Boston Children's Hospital"

scope_default = 'user/*.* patient/*.read openid profile'
scope_nolaunch = 'launch/patient'

class FHIRClient(object):
    """ Instances of this class handle authorizing and talking to SMART on FHIR
    servers.
    
    The settings dictionary supports:
    
        - `app_id`*: Your app/client-id, e.g. 'my_web_app'
        - `api_base`*: The SMART service to connect to, e.g. 'https://fhir-api.smartplatforms.org'
        - `redirect_uri`: The callback/redirect URL for your app, e.g. 'http://localhost:8000/fhir-app/' when testing locally
        - `patient_id`: The patient id against which to operate, if already known
        - `launch_token`: The launch token
    """
    
    def __init__(self, settings=None, state=None, save_func=lambda x:x):
        self.app_id = None
        self.server = None
        self.scope = None
        self.redirect = None
        
        self.launch_context = None
        """ Context parameters supplied by the server during launch. """
        
        self.patient_id = None
        self._patient = None
        
        if save_func is None:
            raise Exception("Must supply a save_func when initializing the SMART client")
        self._save_func = save_func
        
        # init from state
        if state is not None:
            self.from_state(state)
        
        # init from settings dict
        elif settings is not None:
            self.app_id = settings['app_id']
            self.redirect = settings.get('redirect_uri')
            scope = scope_default
            if 'launch_token' in settings:
                self.scope = ' launch:'.join([scope, settings['launch_token']])
            else:
                self.scope = ' '.join([scope_nolaunch, scope])
            self.patient_id = settings.get('patient_id')
            self.server = FHIRServer(self, base_uri=settings['api_base'])
        else:
            raise Exception("Must either supply settings or a state upon client initialization")
    
    
    # MARK: Authorization
    
    @property
    def ready(self):
        """ Returns True if the client is ready to make API calls (e.g. there
        is an access token).
        """
        return self.server.ready if self.server is not None else False
    
    @property
    def authorize_url(self):
        """ The URL to use to receive an authorization token.
        """
        return self.server.authorize_uri if self.server is not None else None
    
    def handle_callback(self, url):
        """ You can call this to have the client automatically handle the
        auth callback after the user has logged in.
        
        :param str url: The complete callback URL
        """
        ctx = self.server.handle_callback(url) if self.server is not None else None
        self._handle_launch_context(ctx)
    
    def reauthorize(self):
        """ Try to reauthorize with the server.
        
        :returns: A bool indicating reauthorization success
        """
        ctx = self.server.reauthorize(self.server) if self.server is not None else None
        self._handle_launch_context(ctx)
        return self.launch_context is not None
    
    def _handle_launch_context(self, ctx):
        if 'patient' in ctx:
            self.patient_id = ctx['patient']        # TODO: TEST THIS!
        self.launch_context = ctx
        self.save_state()
    
    
    # MARK: Current Patient
    
    @property
    def patient(self):
        if self._patient is None and self.patient_id is not None and self.ready:
            try:
                self._patient = patient.Patient.read(self.patient_id, self.server)
            except FHIRUnauthorizedException as e:
                if self.reauthorize():
                    self._patient = patient.Patient.read(self.patient_id, self.server)
        
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
    
    
    # MARK: State
    
    @property
    def state(self):
        return {
            'app_id': self.app_id,
            'scope': self.scope,
            'redirect': self.redirect,
            'patient_id': self.patient_id,
            'server': self.server.state,
            'launch_context': self.launch_context,
        }
    
    def from_state(self, state):
        assert state
        self.app_id = state.get('app_id') or self.app_id
        self.scope = state.get('scope') or self.scope
        self.redirect = state.get('redirect') or self.redirect
        self.patient_id = state.get('patient_id') or self.patient_id
        self.launch_context = state.get('launch_context') or self.launch_context
        self.server = FHIRServer(self, state=state.get('server'))
    
    def save_state (self):
        self._save_func(self.state)

