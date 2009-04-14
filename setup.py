import os
try:
    from setuptools import setup
    extras = {
        'tests_require': ['zope.testing'],
        'test_suite': 'pkginfo.tests',
    }
except ImportError:
    from distutils.core import setup
    extras = {}

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='pkginfo',
    version='0.2',
    description='Query metadatdata from sdists / bdists / installed packages.',
    platform=['Unix', 'Windows'],
    long_description='\n\n'.join([README, CHANGES]),
    keywords='distribution sdist installed metadata',
    url='http://pypi.python.org/pypi/pkginfo/',
    author='Tres Seaver, Agendaless Consulting',
    author_email='tseaver@agendaless.com',
    license='Python',
    classiifiers=[
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Software Distribution',
    ],
    packages=['pkginfo', 'pkginfo.tests'],
    **extras
)
