# -*- coding: utf-8 -*-

import logging
import importlib

from .server import FHIRServer, FHIRUnauthorizedException, FHIRNotFoundException
from .constants import FHIRVersion

__version__ = '5.0.0'
__author__ = 'SMART Platforms Team'
__license__ = 'APACHE2'
__copyright__ = "Copyright 2017 Boston Children's Hospital"

scope_default = 'user/*.* patient/*.read openid profile'
scope_haslaunch = 'launch'
scope_patientlaunch = 'launch/patient'

logger = logging.getLogger(__name__)


class FHIRClient(object):
    """ Instances of this class handle authorizing and talking to SMART on FHIR
    servers.

    The settings dictionary supports:

        - `version`: The FHIRVersion supported
        - `app_id`*: Your app/client-id, e.g. 'my_web_app'
        - `app_secret`*: Your app/client-secret
        - `api_base`*: The FHIR service to connect to, e.g. 'https://fhir-api-dstu2.smarthealthit.org'
        - `redirect_uri`: The callback/redirect URL for your app, e.g. 'http://localhost:8000/fhir-app/' when testing locally
        - `patient_id`: The patient id against which to operate, if already known
        - `scope`: Space-separated list of scopes to request, if other than default
        - `launch_token`: The launch token
    """

    def __init__(self, settings=None, state=None, save_func=lambda x: x):
        self.version = FHIRVersion.R4
        self.app_id = None
        self.app_secret = None
        """ The app-id for the app this client is used in. """

        self.server = None
        self.scope = scope_default
        self.redirect = None
        """ The redirect-uri that will be used to redirect after authorization. """

        self.launch_token = None
        """ The token/id provided at launch, if any. """

        self.launch_context = None
        """ Context parameters supplied by the server during launch. """

        self.wants_patient = True
        """ If true and launched without patient, will add the correct scope
        to indicate that the server should prompt for a patient after login. """

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
            if 'app_id' not in settings:
                raise Exception("Must provide 'app_id' in settings dictionary")
            if 'api_base' not in settings:
                raise Exception("Must provide 'api_base' in settings dictionary")

            self.version = settings.get('version', self.version)
            self.app_id = settings['app_id']
            self.app_secret = settings.get('app_secret')
            self.redirect = settings.get('redirect_uri')
            self.patient_id = settings.get('patient_id')
            self.scope = settings.get('scope', self.scope)
            self.launch_token = settings.get('launch_token')
            self.server = FHIRServer(self, base_uri=settings['api_base'])
        else:
            raise Exception("Must either supply settings or a state upon client initialization")

    # MARK: Authorization

    @property
    def desired_scope(self):
        """ Ensures `self.scope` is completed with launch scopes, according to
        current client settings.
        """
        scope = self.scope
        if self.launch_token is not None:
            scope = ' '.join([scope_haslaunch, scope])
        elif self.patient_id is None and self.wants_patient:
            scope = ' '.join([scope_patientlaunch, scope])
        return scope

    @property
    def ready(self):
        """ Returns True if the client is ready to make API calls (e.g. there
        is an access token or this is an open server).

        :returns: True if the server can make authenticated calls
        """
        return self.server.ready if self.server is not None else False

    def prepare(self):
        """ Returns True if the client is ready to make API calls (e.g. there
        is an access token or this is an open server). In contrast to the
        `ready` property, this method will fetch the server's capability
        statement if it hasn't yet been fetched.

        :returns: True if the server can make authenticated calls
        """
        if self.server:
            if self.server.ready:
                return True
            return self.server.prepare()
        return False

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
        ctx = self.server.reauthorize() if self.server is not None else None
        self._handle_launch_context(ctx)
        return self.launch_context is not None

    def _handle_launch_context(self, ctx):
        logger.debug("SMART: Handling launch context: {0}".format(ctx))
        if 'patient' in ctx:
            # print('Patient id was {0}, row context is {1}'.format(self.patient_id, ctx))
            self.patient_id = ctx['patient']        # TODO: TEST THIS!
        if 'id_token' in ctx:
            logger.warning("SMART: Received an id_token, ignoring")
        self.launch_context = ctx
        self.save_state()

    # MARK: Current Patient

    @property
    def patient(self):
        if self._patient is None and self.patient_id is not None and self.ready:
            patient = importlib.import_module("fhirclient.models.{}.patient".format(self.version))
            try:
                logger.debug("SMART: Attempting to read Patient {0}".format(self.patient_id))
                self._patient = patient.Patient.read(self.patient_id, self.server)
            except FHIRUnauthorizedException:
                if self.reauthorize():
                    logger.debug("SMART: Attempting to read Patient {0} after reauthorizing"
                                 .format(self.patient_id))
                    self._patient = patient.Patient.read(self.patient_id, self.server)
            except FHIRNotFoundException:
                logger.warning("SMART: Patient with id {0} not found".format(self.patient_id))
                self.patient_id = None
            self.save_state()

        return self._patient

    def human_name(self, human_name_instance):
        """ Formats a `HumanName` instance into a string.
        """
        if human_name_instance is None:
            return 'Unknown'

        parts = []
        for n in [human_name_instance.prefix, human_name_instance.given]:
            if n is not None:
                parts.extend(n)
        if human_name_instance.family:
            if isinstance(human_name_instance.family, str):
                parts.append(human_name_instance.family)
            else:
                parts.extend(human_name_instance.family)
        if human_name_instance.suffix and len(human_name_instance.suffix) > 0:
            if len(parts) > 0:
                parts[len(parts)-1] = parts[len(parts)-1]+','
            parts.extend(human_name_instance.suffix)

        return ' '.join(parts) if len(parts) > 0 else 'Unnamed'

    # MARK: State

    def reset_patient(self):
        self.launch_token = None
        self.launch_context = None
        self.patient_id = None
        self._patient = None
        self.save_state()

    @property
    def state(self):
        return {
            'version': self.version,
            'app_id': self.app_id,
            'app_secret': self.app_secret,
            'scope': self.scope,
            'redirect': self.redirect,
            'patient_id': self.patient_id,
            'server': self.server.state,
            'launch_token': self.launch_token,
            'launch_context': self.launch_context,
        }

    def from_state(self, state):
        assert state
        self.version = state.get('version') or self.version
        self.app_id = state.get('app_id') or self.app_id
        self.app_secret = state.get('app_secret') or self.app_secret
        self.scope = state.get('scope') or self.scope
        self.redirect = state.get('redirect') or self.redirect
        self.patient_id = state.get('patient_id') or self.patient_id
        self.launch_token = state.get('launch_token') or self.launch_token
        self.launch_context = state.get('launch_context') or self.launch_context
        self.server = FHIRServer(self, state=state.get('server'))

    def save_state(self):
        self._save_func(self.state)
