How To Contribute
=================

Every open source project lives from the generous help by contributors and fhirclient is no different.

To make participation as pleasant as possible, this project adheres to the [Code of Conduct][] by the Python Software Foundation.

Here are a few hints and rules to get you started:

- Add yourself to the [`AUTHORS.md`][AUTHORS.md] file in an alphabetical fashion.
  Every contribution is valuable and shall be credited.
- No contribution is too small; please submit as many fixes for typos and grammar bloopers as you can!
- Don’t **ever** break backward compatibility.
  If it ever **has** to happen for higher reasons, fhirclient will follow the proven [procedures][] of the Twisted project.
- **Always** add tests and docs for your code.
  This is a hard rule; patches with missing tests or documentation won’t be merged.
  If a feature is not tested or documented, it doesn’t exist.
- Obey [_PEP 8_][pep8] and [_PEP 257_][pep257].
- Write [good commit messages][].
- Ideally, [squash][] your commits, i.e. make your pull requests just one commit.

If you have something great but aren’t sure whether it adheres -- or even can adhere -- to the rules above: **please submit a pull request anyway**!
In the best case, we can mold it into something, in the worst case the pull request gets politely closed.
There’s absolutely nothing to fear.

Thank you for considering to contribute to fhirclient!
If you have any question or concerns, feel free to reach out to us at
<https://groups.google.com/forum/#!forum/smart-on-fhir>


[Code of Conduct]: http://www.python.org/psf/codeofconduct/
[pep8]: http://www.python.org/dev/peps/pep-0008/
[pep257]: http://www.python.org/dev/peps/pep-0257/
[good commit messages]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[squash]: http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html
[AUTHORS.md]: https://github.com/smart-on-fhir/client-py/blob/master/AUTHORS.md
[procedures]: http://twistedmatrix.com/trac/wiki/CompatibilityPolicy
