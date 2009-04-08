pkginfo README
==============

This package provides an API for querying the metadata written by
distutils into the ``PKG-INFO`` directory of a source distriubtion (an
``sdist``).

Basic Usage
-----------

The fundamental abstraction provided by this pacakge is the ``SDist``
class, which is created from a filesystem path to the corresponding
archive::

  >>> from pkginfo import SDist
  >>> mypackage = SDist('tests/mypackage-0.1.tar.gz')

After creation, the ``SDist`` instance will have attributes corrsponding
the the fields defined in PEP 314, lower-cased and transliterated into valid
Python identifiers by mapping hyphens to underscores.  E.g.:

  >>> mypackage.metadata_version
  >>> mypackage.name
  'mypackage'
  >>> mypackage.version
  '0.1'

Fields which are optional under PEP 314, and which have no value set
in their ``PKG-INFO``, will map to the value ``None``::

  >>> mypackage.home_page
  None

Fields which are marked "multiple use" under PEP 314 map onto sequences;
their names are pluralized to indicate the sequence::

  >>> list(mypackage.classifiers)
  ['Development Status :: 4 - Beta', 'Environment :: Console (Text Based)']

"Multiple use" fields with no occurences in the ``PKG-INFO`` file will
map onto an empty sequence::

  >>> list(mypackage.supported_platforms)
  []

