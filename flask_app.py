# -*- coding: utf-8 -*-

import logging
from fhirclient import client
from fhirclient.models.medicationprescription import MedicationPrescription

from flask import Flask, request, redirect, session, jsonify, abort

# app setup
smart_defaults = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhir-api.smartplatforms.org',
    'redirect_uri': 'http://localhost:8000/fhir-app/',
}

app = Flask(__name__)

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

def _get_prescriptions(smart):
    return MedicationPrescription.where().patient(smart.patient_id).perform(smart.server)

def _med_name(prescription):
    if prescription.medication and prescription.medication.resolved and prescription.medication.resolved.name:
        return prescription.medication.resolved.name
    if prescription.medication and prescription.medication.display:
        return prescription.medication.display
    if prescription.text and prescription.text.div:
        return prescription.text.div
    return "Unnamed Medication(TM)"


# views

@app.route('/')
@app.route('/index.html')
def index():
    """ The app's main page.
    """
    smart = _get_smart()
    body = "<h1>Hello</h1>"
    
    if smart.ready and smart.patient is not None:       # "ready" may be true but the access token may have expired, making smart.patient = None
        name = smart.human_name(smart.patient.name[0] if smart.patient.name and len(smart.patient.name) > 0 else 'Unknown')
        gender = smart.patient.gender.coding[0].code if smart.patient.gender.coding and len(smart.patient.gender.coding) > 0 else None
        
        # generate simple body text
        body += "<p>You are authorized and ready to make API requests for <em>{}</em>.</p>".format(name)
        pres = _get_prescriptions(smart)
        if pres is not None:
            body += "<p>{} prescriptions: <ul><li>{}</li></ul></p>".format("His" if 'M' == gender else "Her", '</li><li>'.join([_med_name(m) for m in pres]))
        else:
            body += "<p>(There are no prescriptions for {})</p>".format("him" if 'M' == gender else "her")
        body += """<p><a href="/logout">Logout</a></p>""".format(name)
    else:
        body += """<p>Please <a href="{}">authorize</a>.</p>""".format(smart.authorize_url)
    _save_smart(smart)      # calling `authorize_url` sets a new state, need to save client information. Automate?
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
    import flaskbeaker
    flaskbeaker.FlaskBeaker.setup_app(app)
    
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, port=8000)
