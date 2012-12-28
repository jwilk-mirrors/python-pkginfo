import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    extras = {}
else:
    extras = {
        'test_suite': 'pkginfo.tests',
        'zip_safe': False,
        'extras_require': {
            'testing': ['nose', 'coverage'],
        },
    }

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='pkginfo',
    version='0.9.1',
    description='Query metadatdata from sdists / bdists / installed packages.',
    platforms=['Unix', 'Windows'],
    long_description='\n\n'.join([README, CHANGES]),
    keywords='distribution sdist installed metadata',
    url='http://pypi.python.org/pypi/pkginfo/',
    author='Tres Seaver, Agendaless Consulting',
    author_email='tseaver@agendaless.com',
    license='Python',
    classifiers=[
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.5',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Software Distribution',
    ],
    entry_points={
      'console_scripts': [
        ['pkginfo = pkginfo.commandline:main']
      ]
    },
    packages=['pkginfo', 'pkginfo.tests'],
    **extras
)
