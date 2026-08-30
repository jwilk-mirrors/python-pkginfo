Metadata Versions
=================

The allowed ``PKG-INFO`` fields and their semantics are defined in a series
of PEPs, each of which updates the metadata version field.

- Metadata version 1.0 is specified in `PEP 241`_.
- Metadata version 1.1 is specified in `PEP 314`_.
- Metadata version 1.2 is specified in `PEP 345`_.
- Metadata version 2.0 was proposed in `PEP 426`_. (eventually withdrawn)
- Metadata version 2.1 was proposed in `PEP 566`_.
- Metadata version 2.2 was proposed in `PEP 643`_.
- Metadata version 2.3 was proposed in `PEP 685`_.
- Metadata version 2.4 was proposed in `PEP 639`_. (long approval cycle)
- Metadata version 2.5 was proposed in `PEP 794`_.

A given ``Distribution`` object parses / exposes the attributes which
correspond to the metadata version specified in its ``PKG-INFO``.

You can override the metadata version stored in a given distribution by
passing the specific version (as a string) to its constructor. E.g.,
updating the metadata version here in order to expose the classifiers,
which were not defined under version '1.0':

.. doctest::

  >>> from pkginfo import SDist
  >>> mypackage = SDist('docs/examples/mypackage-0.1.tar.gz',
  ...                   metadata_version='1.1')
  >>> print([str(x) for x in mypackage.classifiers])
  ['Development Status :: 4 - Beta', 'Environment :: Console (Text Based)']

.. _`PEP 241`: http://svn.python.org/projects/peps/trunk/pep-0241.txt
.. _`PEP 314`: http://svn.python.org/projects/peps/trunk/pep-0314.txt
.. _`PEP 345`: http://svn.python.org/projects/peps/trunk/pep-0345.txt
.. _`PEP 426`: http://svn.python.org/projects/peps/trunk/pep-0426.txt
.. _`PEP 566`: http://svn.python.org/projects/peps/trunk/pep-0566.txt
.. _`PEP 639`: http://svn.python.org/projects/peps/trunk/pep-0639.txt
.. _`PEP 643`: http://svn.python.org/projects/peps/trunk/pep-0643.txt
.. _`PEP 685`: http://svn.python.org/projects/peps/trunk/pep-0685.txt
.. _`PEP 794`: http://svn.python.org/projects/peps/trunk/pep-0794.txt
