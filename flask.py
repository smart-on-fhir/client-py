# -*- coding: utf-8 -*-

import logging
from fhirclient import client

from flask import Flask, request, render_template, session, jsonify, abort
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware


smart_defaults = {
	'app_id': 'my_web_app',
	'api_base': 'https://fhir-api.smartplatforms.org',
	'redirect': 'http://localhost:8000/fhir-app/',
	'scope': 'launch/patient user/*.* patient/*.read openid profile',
	'launch_token': 1288992,
}


# session setup

session_opts = {
	'session.type': 'file',
	'session.timeout': 3600,
	'session.cookie_expires': 3600,
	'session.data_dir': './session_data',
	'session.auto': True
}

class BeakerSessionInterface(SessionInterface):
	def open_session(self, app, request):
		session = request.environ['beaker.session']
		return session
	def save_session(self, app, session, response):
		session.save()


# app setup

app = Flask(__name__)

def _get_smart():
	state = session.get('state')
	if state:
		return client.FHIRClient(state=state)
	return client.FHIRClient(settings=smart_defaults)

def _logout():
	del session['state']


# routes

@app.route('/')
@app.route('/index.html')
def index():
	""" The app's main page.
	"""
	smart = _get_smart()
	return """<h1>Hello</h1><p>Please <a href="{}">authorize</a>.</p>""".format(smart.authorize_url)


@app.route('/fhir-app/')
def callback():
	""" OAuth2 callback interception.
	"""
	smart = _get_smart()
	try:
		smart.handle_callback(request.url)
	except Exception as e:
		return "<h1>Authorization Error</h1><p>{}</p>".format(e)
	
	return 'ok'


@app.route('/logout')
def logout():
	self._logout()
	return "Bye"


# start the app
if '__main__' == __name__:
	logging.basicConfig(level=logging.DEBUG)
	app.run(debug=True, port=8000)
