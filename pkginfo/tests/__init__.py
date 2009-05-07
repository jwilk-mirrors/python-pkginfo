# requirements

def additional_tests():
    import doctest
    return doctest.DocFileSuite('../../docs/index.rst',
                                module_relative=True,
                               )

def _checkSample(testcase, installed):
    testcase.assertEqual(installed.metadata_version, '1.0')
    testcase.assertEqual(installed.name, 'pkginfo')
    testcase.assertEqual(installed.version, '0.3')
    testcase.assertEqual(installed.keywords,
                        'distribution sdist installed metadata' )
    testcase.assertEqual(list(installed.classifiers),
                         [
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Software Distribution',
    ])
    testcase.assertEqual(list(installed.supported_platforms), [])
