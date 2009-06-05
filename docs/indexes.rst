Distribution Indexes
=====================

An ``Index`` is conceptually a set of ``Distribution`` objects, with some
additional behavior for managing the set as a whole.

.. doctest::

  >>> from pkginfo import Distribution
  >>> from pkginfo import Index
  >>> index = Index()
  >>> list(index)
  []
  >>> d1 = Distribution()
  >>> d1.name = 'foo'
  >>> d1.version = '1.0'
  >>> index.add(d1)
  >>> list(index)
  ['foo-1.0']
  >>> d2 = Distribution()
  >>> d2.name = 'foo'
  >>> d2.version = '1.1'
  >>> index.add(d2)
  >>> sorted(list(index))
  ['foo-1.0', 'foo-1.1']

