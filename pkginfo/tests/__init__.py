# requirements

def additional_tests():
    import doctest
    import unittest
    return unittest.TestSuite((
        doctest.DocFileSuite('../../docs/index.rst',
                                module_relative=True),
        doctest.DocFileSuite('../../docs/distributions.rst',
                                module_relative=True),
        doctest.DocFileSuite('../../docs/metadata.rst',
                                module_relative=True),
        doctest.DocFileSuite('../../docs/indexes.rst',
                                module_relative=True),
    ))


def _checkSample(testcase, installed):
    try:
        import pkg_resources
    except ImportError: # no setuptools :(
        pass
    else:
        version = pkg_resources.require('pkginfo')[0].version
        testcase.assertEqual(installed.version, version)
    testcase.assertEqual(installed.name, 'pkginfo')
    testcase.assertEqual(installed.keywords,
                        'distribution sdist installed metadata' )
    testcase.assertEqual(list(installed.supported_platforms), [])

def _checkClassifiers(testcase, installed):
    testcase.assertEqual(list(installed.classifiers),
                         [
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: Implementation :: CPython',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Software Distribution',
    ])


def _defaultMetadataVersion():
    import platform
    import sys
    if platform.python_implementation() == 'PyPy':
        return '1.0'
    return  sys.version_info >= (2, 7) and '1.1' or '1.0'
