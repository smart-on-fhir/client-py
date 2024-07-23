# Maintainer Notes

## Building Distribution

    pip install -U build
    python3 -m build

## Incrementing the lib version

- Edit `fhirclient/client.py` and change the `__version__` field.
- Edit `docs/Doxyfile` and change the `PROJECT_NUMBER` field.

## Cutting a new release

1. Make sure that the version is correct in the source (see above for update instructions).
2. Update the docs
3. Release on GitHub
4. Announce on Zulip

### Docs Generation

Docs are generated with [Doxygen](https://www.doxygen.nl/)
and [doxypypy](https://github.com/Feneric/doxypypy).
You can install doxypypy via pip: `pip install doxypypy`.
Then you can just run Doxygen. Configuration is stored in `docs/Doxyfile`.

Running Doxygen will put the generated HTML documentation into `docs/html`.
Those files make up the content of the `gh-pages` branch.
I usually perform a second checkout of the _gh-pages_ branch and copy the HTML files over, with:

    doxygen docs/Doxyfile
    rsync -a docs/html/ ../client-py-web/

### Release on GitHub

Just create a new release in GitHub and create a corresponding tag.

This will also cause the `pypi.yaml` GitHub Action to fire, uploading to PyPI.

### Announce the release

Make a post in the [Zulip channel](https://chat.fhir.org/#narrow/stream/179218-python) for python.
