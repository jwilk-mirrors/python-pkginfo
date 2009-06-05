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
    testcase.assertEqual(installed.name, 'pkginfo')
    testcase.assertEqual(installed.version, '0.4.1')
    testcase.assertEqual(installed.keywords,
                        'distribution sdist installed metadata' )
    testcase.assertEqual(list(installed.supported_platforms), [])

def _checkClassifiers(testcase, installed):
    testcase.assertEqual(list(installed.classifiers),
                         [
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Software Distribution',
    ])
