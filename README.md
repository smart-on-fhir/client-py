SMART FHIR Client
=================

This is _fhirclient_, a flexible Python client for [FHIR][] servers supporting the [SMART on FHIR][smart] protocol.
The client is compatible with Python 2.7.10 and Python 3.

Client versioning is not identical to FHIR versioning.
The `master` branch is usually on the latest version of the client as shown below, possibly on bugfix releases thereof.
The `develop` branch should be on recent freezes, and the `feature/latest-ci` branch is periodically updated to the latest FHIR continuous integration builds.

   Version |          FHIR | &nbsp;
-----------|---------------|---
   **x.x** |       `1.8.0` | (STU-3 Ballot, Jan 2017)
   **x.x** |       `1.6.0` | (STU-3 Ballot, Sep 2016)
 **1.0.3** |       `1.0.2` | (DSTU 2)
   **1.0** |       `1.0.1` | (DSTU 2)
   **0.5** |  `0.5.0.5149` | (DSTU 2 Ballot, May 2015)
 **0.0.4** | `0.0.82.2943` | (DSTU 1)
 **0.0.3** | `0.0.82.2943` | (DSTU 1)
 **0.0.2** | `0.0.82.2943` | (DSTU 1)


Installation
------------

    pip install fhirclient


Documentation
-------------

Technical documentation is available at [docs.smarthealthit.org/client-py/][docs].

### Client Use

To connect to a SMART on FHIR server (or any open FHIR server), you can use the `FHIRClient` class.
It will initialize and handle a `FHIRServer` instance, your actual handle to the FHIR server you'd like to access.

##### Read Data from Server

To read a given patient from an open FHIR server, you can use:

```python
from fhirclient import client
settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhir-open-api-dstu2.smarthealthit.org'
}
smart = client.FHIRClient(settings=settings)

import fhirclient.models.patient as p
patient = p.Patient.read('hca-pat-1', smart.server)
patient.birthDate.isostring
# '1963-06-12'
smart.human_name(patient.name[0])
# 'Christy Ebert'
```

If this is a protected server, you will first have to send your user to the authorize endpoint to log in.
Just call `smart.authorize_url` to obtain the correct URL.
You can use `smart.prepare()`, which will return `False` if the server is protected and you need to authorize.
The `smart.ready` property has the same purpose, it will however not retrieve the server's _CapabilityStatement_ resource and hence is only useful as a quick check whether the server instance is ready.

```python
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

You can work with the `FHIRServer` class directly, without using `FHIRClient`, but this is not recommended:

```python
smart = server.FHIRServer(None, 'https://fhir-open-api-dstu2.smarthealthit.org')
import fhirclient.models.patient as p
patient = p.Patient.read('hca-pat-1', smart)
patient.name[0].given
# ['Christy']
```

##### Search Records on Server

You can also search for resources matching a particular set of criteria:

```python
smart = client.FHIRClient(settings=settings)
import fhirclient.models.procedure as p
search = p.Procedure.where(struct={'subject': 'hca-pat-1', 'status': 'completed'})
procedures = search.perform_resources(smart.server)
for procedure in procedures:
    procedure.as_json()
    # {'status': u'completed', 'code': {'text': u'Lumpectomy w/ SN', ...

# to get the raw Bundle instead of resources only, you can use:
bundle = search.perform(smart.server)
```

### Data Model Use

The client contains data model classes, built using [fhir-parser][], that handle (de)serialization and allow to work with FHIR data in a Pythonic way.
Starting with version 1.0.5, data model validity are enforced to a certain degree.

#### Initialize Data Model

```python
import fhirclient.models.patient as p
import fhirclient.models.humanname as hn
patient = p.Patient({'id': 'patient-1'})
patient.id
# prints `patient-1`

name = hn.HumanName()
name.given = ['Peter']
name.family = ['Parker']
patient.name = [name]
patient.as_json()
# prints patient's JSON representation, now with id and name

name.given = 'Peter'
patient.as_json()
# throws FHIRValidationError:
# {root}:
#   name:
#     given:
#       Expecting property "given" on <class 'fhirclient.models.humanname.HumanName'> to be list, but is <class 'str'>
```

#### Initialize from JSON file

```python
import json
import fhirclient.models.patient as p
with open('path/to/patient.json', 'r') as h:
    pjs = json.load(h)
patient = p.Patient(pjs)
patient.name[0].given
# prints patient's given name array in the first `name` property
```

### Flask App

Take a look at [`flask_app.py`][flask_app] to see how you can use the client in a simple (Flask) app.
This app starts a webserver, listening on [_localhost:8000_](http://localhost:8000), and prompts you to login to our sandbox server and select a patient.
It then goes on to retrieve the selected patient's demographics and med prescriptions and lists them in a simple HTML page.

The Flask demo app has separate requirements.
Clone the _client-py_ repository, then best create a virtual environment and install the needed packages like so:

    git clone https://github.com/smart-on-fhir/client-py.git
    cd client-py
    virtualenv -p python3 env
    . env/bin/activate
    pip install -r requirements_flask_app.txt
    python flask_app.py


Building Distribution
---------------------

    pip install -r requirements.txt
    python setup.py sdist
    python setup.py bdist_wheel


### Incrementing the lib version

    bumpversion patch
    bumpversion minor
    bumpversion major


Docs Generation
---------------

Docs are generated with [Doxygen][] and [doxypypy][].
You can install doxypypy via pip: `pip install doxypypy`.
Then you can just run Doxygen, configuration is stored in the `Doxyfile`.

Running Doxygen will put the generated documentation into `docs`, the HTML files into `docs/html`.
Those files make up the content of the `gh-pages` branch.
I usually perform a second checkout of the _gh-pages_ branch and copy the html files over, with:

    doxygen
    rsync -a docs/html/ ../client-py-web/


PyPi Publishing (notes for SMART team)
--------------------------------------

Using setuptools (*Note*: Alternatively, you can use twine https://pypi.python.org/pypi/twine/):

### Make sure that you have the PyPi account credentials in your account

    copy server.smarthealthit.org:/home/fhir/.pypirc to ~/.pypirc

### Test the build

    python setup.py sdist
    python setup.py bdist_wheel

### Upload the packages to PyPi

    python setup.py sdist upload -r pypi
    python setup.py bdist_wheel upload -r pypi


[fhir]: http://www.hl7.org/implement/standards/fhir/
[smart]: http://docs.smarthealthit.org
[fhir-parser]: https://github.com/smart-on-fhir/fhir-parser
[docs]: https://smart-on-fhir.github.io/client-py
[flask_app]: https://github.com/smart-on-fhir/client-py/blob/master/flask_app.py
[doxygen]: http://www.stack.nl/~dimitri/doxygen
[doxypypy]: https://github.com/Feneric/doxypypy
