pkginfo documentation
=====================

Contents:

.. toctree::
   :maxdepth: 2

Distribution Types
------------------

The fundamental abstraction provided by this pacakge is the ``Distribution``
base class.  Implementations exist for specific cases:  source distributions,
binary distributions, and installed distributions.

.. doctest::

  >>> from pkginfo import Distribution
  >>> from pkginfo import SDist
  >>> assert issubclass(SDist, Distribution)
  >>> from pkginfo import Installed
  >>> assert issubclass(Installed, Distribution)


Introspecting Source Distributions
----------------------------------

``SDist`` objects are created from a filesystem path to the corresponding
archive, which should have been created via the ``sdist`` command from
distutils:

.. doctest::

  >>> mypackage = SDist('docs/examples/mypackage-0.1.tar.gz')

After creation, the ``SDist`` instance will have attributes corrsponding
the the fields defined in PEP 314, lower-cased and transliterated into valid
Python identifiers by mapping hyphens to underscores.  E.g.:

.. doctest::

  >>> print mypackage.metadata_version
  1.0
  >>> print mypackage.name
  mypackage
  >>> print mypackage.version
  0.1

Fields which are optional under PEP 314, and which have no value set
in their ``PKG-INFO``, will map to the value ``None``:

.. doctest::

  >>> print mypackage.keywords
  None

Fields which are marked "multiple use" under PEP 314 map onto sequences;
their names are pluralized to indicate the sequence:

.. doctest::

  >>> print list(mypackage.classifiers)
  ['Development Status :: 4 - Beta', 'Environment :: Console (Text Based)']

"Multiple use" fields with no occurences in the ``PKG-INFO`` file will
map onto an empty sequence:

.. doctest::

  >>> print list(mypackage.supported_platforms)
  []


Introspecting Installed Packages
--------------------------------

``Installed`` objects are created from either a module object or its
dotted name.

.. doctest::

  >>> dotted = Installed('pkginfo')
  >>> import pkginfo
  >>> direct = Installed(pkginfo)

After that, they have the same metadata as other ``Distribution`` objects,
assuming that the package on which they were based has a discoverable
'.egg-info' file / directory.  To be discoverable, the '.egg-info' must
either be located inside the package (e.g., created via ``setup.py develop``
under setuptools), or adjacent to the package (e.g., created via
``setup.py instlall``).
