Distribution Types
==================

The fundamental abstraction provided by this pacakge is the ``Distribution``
base class.  Implementations exist for specific cases:  source distributions,
binary distributions, installed pakcages, and development checkouts.

.. doctest::

  >>> from pkginfo import Distribution
  >>> from pkginfo import SDist
  >>> assert issubclass(SDist, Distribution)
  >>> from pkginfo import UnpackedSDist
  >>> assert issubclass(UnpackedSDist, SDist)
  >>> from pkginfo import BDist
  >>> assert issubclass(BDist, Distribution)
  >>> from pkginfo import Wheel
  >>> assert issubclass(Wheel, Distribution)
  >>> from pkginfo import Installed
  >>> assert issubclass(Installed, Distribution)
  >>> from pkginfo import Develop
  >>> assert issubclass(Develop, Distribution)

Introspecting Source Distributions
----------------------------------

``SDist`` objects are created from a filesystem path to the corresponding
archive, which should have been created via the ``sdist`` command from
distutils:

.. doctest::

  >>> mypackage = SDist('docs/examples/mypackage-0.1.tar.gz')

After creation, the ``SDist`` instance will have attributes corrsponding
the the fields defined in the PEP corresponding to the metadata version,
lower-cased and transliterated into valid Python identifiers by mapping
hyphens to underscores.  E.g.:

.. doctest::

  >>> print(mypackage.metadata_version)
  1.0
  >>> print(mypackage.name)
  mypackage
  >>> print(mypackage.version)
  0.1

Fields which are optional under the PEP, and which have no value set
in their ``PKG-INFO``, will map to the value ``None``:

.. doctest::

  >>> print(mypackage.keywords)
  None

Fields which are marked "multiple use" under the PEP map onto sequences;
their names are pluralized to indicate the sequence.  "Multiple use" fields
with no occurences in the ``PKG-INFO`` file will map onto an empty sequence:

.. doctest::

  >>> print(list(mypackage.supported_platforms))
  []

See `Metadata Versions <metadata.html>`_ for an example with a non-empty,
"multiple-use" field.

Introspecting Unpacked Source Distributions
-------------------------------------------

You can also introspect a previously-unpacked package with ``UnpackedSDist``
either by passing it the path to the unpacked package, or by passing it the
setup.py at the top level:

.. doctest::

  >>> mypackage = UnpackedSDist('docs/examples/mypackage-0.1')
  >>> print(mypackage.name)
  mypackage
  >>> myotherpackage = UnpackedSDist('docs/examples/mypackage-0.1/setup.py')
  >>> print(myotherpackage.name)
  mypackage

``UnpackedSDist`` objects are most useful in conjuction with distutils to
produce sdists that want complex behavior for determining what metadata to use;
these sdists normally break when installed with ``pip``, because metadata in an
sdist is regenerated when pip installed. You can achieve this in your
`setup.py` as follows:

.. code::

  >>> from setuptools import dist, setup
  >>> dist.Distribution(dict(setup_requires='pkginfo'))
  >>> from pkginfo import UnpackedSDist

  >>> try:
  ...     d = UnpackedSDist(__file__)
  ...     VERSION = d.version
  ... except ValueError:
  ...     VERSION = (version_from_source_control() or
  ...                os.getenv('VERSION', '1.0'))
  >>> setup(name='mypackage', version=VERSION)

Introspecting Binary Distributions
----------------------------------

``BDist`` objects are created from the filename, which should have been
generated via ``setup.py bdist_egg``.

.. doctest::

  >>> mypackage = BDist('docs/examples/mypackage-0.1-py2.6.egg')

After that, they have the same metadata as other ``Distribution`` objects,

Introspecting Wheels
--------------------

``Wheel`` objects are created from the filename, which should have been
generated via ``setup.py bdist_wheel``.

.. doctest::

  >>> mypackage = Wheel('docs/examples/mypackage-0.1-cp26-none-linux_x86_64.whl')

After that, they have the same metadata as other ``Distribution`` objects,


Introspecting Installed Packages
--------------------------------

``Installed`` objects are created from either a module object or its
dotted name.  Note that this feature only works in Python 2.6 or later:
earlier Python versions did not record ``PKG-INFO`` for installed packages.

.. doctest::

  >>> import sys
  >>> if sys.version_info >= (2,6):
  ...    dotted = Installed('pkginfo')
  ...    import pkginfo
  ...    direct = Installed(pkginfo)

After that, they have the same metadata as other ``Distribution`` objects,
assuming that the package on which they were based has a discoverable
'.egg-info' file / directory.  To be discoverable, the '.egg-info' must
either be located inside the package (e.g., created via ``setup.py develop``
under setuptools), or adjacent to the package (e.g., created via
``setup.py instlall``).


Introspecting Development Checkouts
-----------------------------------

``Develop`` objects are created from a path to a checkout containing
a ``PKG-iNFO`` file, e.g., created by running ``setup.py develop`` under
setuptools.

.. doctest::

  >>> develop = Develop('.')

After that, they have the same metadata as other ``Distribution`` objects.
