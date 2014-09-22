# -*- coding: utf-8 -*-

import logging
from fhirclient import client

from flask import Flask, request, redirect, session, jsonify, abort
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware


app_secret_key = 'aeimoalk7o'
smart_defaults = {
	'app_id': 'my_web_app',
	'api_base': 'https://fhir-api.smartplatforms.org',
	'redirect_uri': 'http://localhost:8000/fhir-app/',
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
app.secret_key = app_secret_key

def _get_smart():
	state = session.get('state')
	if state:
		return client.FHIRClient(state=state)
	return client.FHIRClient(settings=smart_defaults)

def _save_smart(client):
	session['state'] = client.state

def _logout():
	if 'state' in session:
		del session['state']


# views

@app.route('/')
@app.route('/index.html')
def index():
	""" The app's main page.
	"""
	smart = _get_smart()
	body = "<h1>Hello</h1>"
	if smart.ready:
		body += """<p>You are authorized and ready to make API requests.</p><p><a href="/logout">Logout</a></p>"""
	else:
		body += """<p>Please <a href="{}">authorize</a>.</p>""".format(smart.authorize_url)
	_save_smart(smart)		# calling `authorize_url` sets a new state, need to save client information. Automate?
	return body


@app.route('/fhir-app/')
def callback():
	""" OAuth2 callback interception.
	"""
	smart = _get_smart()
	try:
		smart.handle_callback(request.url)
		_save_smart(smart)
	except Exception as e:
		return """<h1>Authorization Error</h1><p>{}</p><p><a href="/">Start over</a></p>""".format(e)
	return redirect('/')


@app.route('/logout')
def logout():
	_logout()
	return redirect('/')


# start the app
if '__main__' == __name__:
	logging.basicConfig(level=logging.DEBUG)
	app.run(debug=True, port=8000)
