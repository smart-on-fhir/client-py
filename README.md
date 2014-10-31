fhirclient
==========

To install using PIP
--------------------

    pip install fhirclient


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
You will need to install doxypypy the old-fashioned way, checking out the repo and issuing `python setup.py install`.
Then you can just run Doxygen, configuration is stored in the `Doxyfile`.

Running Doxygen will put the generated documentation into `docs`, the HTML files into `docs/html`.
Those files make up the content of the `gh-pages` branch.
I usually perform a second checkout of the _gh-pages_ branch and copy the html files over, with:

    doxygen
    rsync -a docs/html/ ../client-py-web/


[docs]: https://smart-on-fhir.github.io/client-py
[doxygen]: http://www.stack.nl/~dimitri/doxygen
[doxypypy]: https://github.com/Feneric/doxypypy
