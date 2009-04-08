import os
try:
    from setuptools import setup
except ImportError:
    from distutils import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='pkginfo',
    version='0.1',
    description='Query PKG-INFO data from sdist archives.',
)
