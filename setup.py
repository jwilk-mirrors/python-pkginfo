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
            'testing': ['pytest', 'pytest-cov'],
        },
    }

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='pkginfo',
    version='1.9.2',
    description='Query metadatdata from sdists / bdists / installed packages.',
    platforms=['Unix', 'Windows'],
    long_description='\n\n'.join([README, CHANGES]),
    keywords='distribution sdist installed metadata',
    url='https://code.launchpad.net/~tseaver/pkginfo/trunk',
    author='Tres Seaver, Agendaless Consulting',
    author_email='tseaver@agendaless.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Software Distribution',
    ],
    entry_points={
        'console_scripts': [
            'pkginfo = pkginfo.commandline:main',
        ]
    },
    packages=['pkginfo', 'pkginfo.tests'],
    python_requires='>=3.6',
    **extras
)
