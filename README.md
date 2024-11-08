# SMART FHIR Client

This is _fhirclient_, a flexible Python client for [FHIR][] servers supporting the [SMART on FHIR][smart] protocol.

Client versioning is not identical to FHIR versioning.
The `main` branch is usually on the latest version of the client, as shown below, and possibly on their bugfix releases.
The `develop` branch should be on recent freezes, and the `feature/latest-ci` branch is periodically updated to the latest FHIR continuous integration builds.

   Version | FHIR         | &nbsp;
-----------|--------------|---------
 **4.2.0** |       `4.0.1` | (R4)
 **4.0.0** |       `4.0.0` | (R4)
 **3.0.0** |       `3.0.0` | (STU-3)
   **x.x** |       `1.8.0` | (STU-3 Ballot, Jan 2017)
   **x.x** |       `1.6.0` | (STU-3 Ballot, Sep 2016)
 **1.0.3** |       `1.0.2` | (DSTU 2)
   **1.0** |       `1.0.1` | (DSTU 2)
   **0.5** |  `0.5.0.5149` | (DSTU 2 Ballot, May 2015)
 **0.0.4** | `0.0.82.2943` | (DSTU 1)
 **0.0.3** | `0.0.82.2943` | (DSTU 1)
 **0.0.2** | `0.0.82.2943` | (DSTU 1)


## Installation

    pip install fhirclient


## Documentation

Technical documentation is available at [docs.smarthealthit.org/client-py/][docs].

### Client Use

To connect to a SMART on FHIR server (or any open FHIR server), you can use the `FHIRClient` class.
It will initialize and handle a `FHIRServer` instance, your actual handle to the FHIR server you'd like to access.

##### Read Data from Server

To read a given patient from an open FHIR server, you can use:

```python
from fhirclient import client
from fhirclient.models.patient import Patient

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r4.smarthealthit.org'
}
smart = client.FHIRClient(settings=settings)

patient = Patient.read('2cda5aad-e409-4070-9a15-e1c35c46ed5a', smart.server)
print(patient.birthDate.isostring)
# '1992-07-03'
print(smart.human_name(patient.name[0]))
# 'Mr. Geoffrey Abbott'
```
If this is a protected server, you will first have to send your user to the authorization endpoint to log in.
Just call `smart.authorize_url` to obtain the correct URL.
You can use `smart.prepare()`, which will return `False` if the server is protected and you need to authorize.
The `smart.ready` property has the same purpose. However, it will not retrieve the server's _CapabilityStatement_ resource and hence is only fit as a quick check whether the server instance is ready.

```python
from fhirclient import client

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r4.smarthealthit.org'
}
smart = client.FHIRClient(settings=settings)

smart.ready
# prints `False`
smart.prepare()
# prints `True` after fetching CapabilityStatement
smart.ready
# prints `True`
smart.prepare()
# prints `True` immediately
smart.authorize_url
# is `None`
```

You can work with the `FHIRServer` class directly without using `FHIRClient`. But this is not recommended:

```python
from fhirclient import server
from fhirclient.models.patient import Patient

smart = server.FHIRServer(None, 'https://r4.smarthealthit.org')
patient = Patient.read('2cda5aad-e409-4070-9a15-e1c35c46ed5a', smart)
print(patient.name[0].given)
# ['Geoffrey']
```

##### Search Records on Server

You can also search for resources matching a particular set of criteria:

```python
from fhirclient import client
from fhirclient.models.encounter import Encounter
from fhirclient.models.procedure import Procedure

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r4.smarthealthit.org'
}
smart = client.FHIRClient(settings=settings)

search = Encounter.where(struct={'subject': '2cda5aad-e409-4070-9a15-e1c35c46ed5a', 'status': 'finished'})
print({res.type[0].text for res in search.perform_resources_iter(smart.server)})
# {'Encounter for symptom', 'Encounter for check up (procedure)'}

# to include the resources referred to by the encounter via `subject` in the results
search = search.include('subject')
print({res.resource_type for res in search.perform_resources_iter(smart.server)})
# {'Encounter', 'Patient'}

# to include the Procedure resources which refer to the encounter via `encounter`
search = search.include('encounter', Procedure, reverse=True)
print({res.resource_type for res in search.perform_resources_iter(smart.server)})
# {'Encounter', 'Patient', 'Procedure'}

# to get the raw Bundles instead of resources only, you can use:
bundles = search.perform_iter(smart.server)
print({entry.resource.resource_type for bundle in bundles for entry in bundle.entry})
# {'Encounter', 'Patient', 'Procedure'}
```

### Data Model Use

The client contains data model classes, built using [fhir-parser][], that handle (de)serialization and allow you to work with FHIR data in a Pythonic way. From version 1.0.5, the validity of the data model is enforced to a certain extent.

#### Initialize Data Model

```python
from fhirclient.models.patient import Patient
from fhirclient.models.humanname import HumanName

patient = Patient({'id': 'patient-1'})
print(patient.id)
# patient-1

name = HumanName()
name.given = ['Peter']
name.family = 'Parker'
patient.name = [name]
print(patient.as_json())
# {'id': 'patient-1', 'name': [{'family': 'Parker', 'given': ['Peter']}], 'resourceType': 'Patient'}

name.given = 'Peter'
print(patient.as_json())
# throws FHIRValidationError:
# {root}:
#   name.0:
#     given:
#       Expecting property "given" on <class 'fhirclient.models.humanname.HumanName'> to be list, but is <class 'str'>
```

#### Initialize from JSON

```python
import json
from fhirclient.models.patient import Patient

pjs = json.loads('{"name": [{"given": ["Peter"]}], "resourceType": "Patient"}')
patient = Patient(pjs)
print(patient.name[0].given)
# ['Peter']
```

### Flask App

Take a look at
[flask_app.py](https://github.com/smart-on-fhir/client-py/blob/main/demos/flask/flask_app.py)
to see how you can use the client in a simple (Flask) app.

This demo requires a server that is capable of SMART OAuth logins for patients,
so make sure you have such a server ready first.

This app will start a web server,
listen on [_localhost:8000_](http://localhost:8000),
and prompt you to log in to our sandbox server and select a patient.
It then retrieves the selected patient's demographics and med prescriptions
and lists them on a simple HTML page.

The Flask demo app has separate requirements.
Clone the _client-py_ repository,
then create a virtual environment (not compulsory but recommended)
and install the needed packages as shown:

    git clone https://github.com/smart-on-fhir/client-py.git
    cd client-py/demos/flask
    python3 -m venv env
    . env/bin/activate
    pip install -r requirements.txt
    # Edit flask_app.py and put your own server's URL as api_base.
    ./flask_app.py


[fhir]: http://www.hl7.org/implement/standards/fhir/
[smart]: http://docs.smarthealthit.org
[fhir-parser]: https://github.com/smart-on-fhir/fhir-parser
[docs]: https://smart-on-fhir.github.io/client-py
