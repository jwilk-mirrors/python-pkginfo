:mod:`pkginfo` documentation
============================

This package provides an API for querying the distutils metadata written in
the ``PKG-INFO`` file inside a source distribution (an ``sdist``) or a
binary distribution (e.g., created by running ``bdist_egg`` or
``bdist_wheel``).  It can also query the ``EGG-INFO`` directory of an
installed distribution, and the ``*.egg-info`` stored in a "development
checkout" (e.g, created by running ``setup.py develop``).

Contents:

.. toctree::
   :maxdepth: 2

   distributions
   metadata
   indexes
