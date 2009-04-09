import unittest

class SDistTests(unittest.TestCase):

    def _getTargetClass(self):
        from pkginfo.sdist import SDist
        return SDist

    def _makeOne(self, filename=None):
        return self._getTargetClass()(filename)

    def test_ctor_no_filename(self):
        sdist = self._makeOne()
        self.assertEqual(sdist.metadata_version, None)
        self.assertEqual(sdist.name, None)
        self.assertEqual(sdist.version, None)
        self.assertEqual(sdist.platforms, ())
        self.assertEqual(sdist.supported_platforms, ())
        self.assertEqual(sdist.summary, None)
        self.assertEqual(sdist.description, None)
        self.assertEqual(sdist.keywords, None)
        self.assertEqual(sdist.home_page, None)
        self.assertEqual(sdist.download_url, None)
        self.assertEqual(sdist.author, None)
        self.assertEqual(sdist.author_email, None)
        self.assertEqual(sdist.license, None)
        self.assertEqual(sdist.classifiers, ())
        self.assertEqual(sdist.requires, ())
        self.assertEqual(sdist.provides, ())
        self.assertEqual(sdist.obsoletes, ())

    def _checkSample(self, sdist, filename):
        self.assertEqual(sdist.filename, filename)
        self.assertEqual(sdist.metadata_version, '1.0')
        self.assertEqual(sdist.name, 'mypackage')
        self.assertEqual(sdist.version, '0.1')
        self.assertEqual(sdist.keywords, None)
        self.assertEqual(list(sdist.classifiers),
                         ['Development Status :: 4 - Beta',
                          'Environment :: Console (Text Based)',
                         ])
        self.assertEqual(list(sdist.supported_platforms), [])

    def test_ctor_w_gztar(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.tar.gz' % d
        sdist = self._makeOne(filename)
        self._checkSample(sdist, filename)

    def test_ctor_w_bztar(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.tar.bz2' % d
        sdist = self._makeOne(filename)
        self._checkSample(sdist, filename)

    def test_ctor_w_zip(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1.zip' % d
        sdist = self._makeOne(filename)
        self._checkSample(sdist, filename)

    def test_read_Metadata_Version(self):
        sdist = self._makeOne()
        sdist.read('Metadata-Version: 1.3')
        self.assertEqual(sdist.metadata_version, '1.3')

    def test_read_Name(self):
        sdist = self._makeOne()
        sdist.read('Name: foobar')
        self.assertEqual(sdist.name, 'foobar')

    def test_read_Version(self):
        sdist = self._makeOne()
        sdist.read('Version: 2.1.3b5')
        self.assertEqual(sdist.version, '2.1.3b5')

    def test_read_Platform_single(self):
        sdist = self._makeOne()
        sdist.read('Platform: Plan9')
        self.assertEqual(list(sdist.platforms), ['Plan9'])

    def test_read_Platform_multiple(self):
        sdist = self._makeOne()
        sdist.read('Platform: Plan9\nPlatform: AIX')
        self.assertEqual(list(sdist.platforms), ['Plan9', 'AIX'])

    def test_read_Supported_Platform_single(self):
        sdist = self._makeOne()
        sdist.read('Supported-Platform: Plan9')
        self.assertEqual(list(sdist.supported_platforms), ['Plan9'])

    def test_read_Supported_Platform_multiple(self):
        sdist = self._makeOne()
        sdist.read('Supported-Platform: i386-win32\n'
                   'Supported-Platform: RedHat 7.2')
        self.assertEqual(list(sdist.supported_platforms),
                        ['i386-win32', 'RedHat 7.2'])

    def test_read_Summary(self):
        sdist = self._makeOne()
        sdist.read('Summary: Package for foo')
        self.assertEqual(sdist.summary, 'Package for foo')

    def test_read_Description(self):
        sdist = self._makeOne()
        sdist.read('Description: This package enables integration with\n'
                   '       foo servers.')
        self.assertEqual(sdist.description,
                         'This package enables integration with\n'
                         ' foo servers.')

    def test_read_Keywords(self):
        sdist = self._makeOne()
        sdist.read('Keywords: bar foo qux')
        self.assertEqual(sdist.keywords, 'bar foo qux')

    def test_read_Home_page(self):
        sdist = self._makeOne()
        sdist.read('Home-page: http://example.com/package')
        self.assertEqual(sdist.home_page, 'http://example.com/package')

    def test_read_Download_URL(self):
        sdist = self._makeOne()
        sdist.read('Download-URL: http://example.com/package/mypackage-0.1.zip')
        self.assertEqual(sdist.download_url,
                         'http://example.com/package/mypackage-0.1.zip')

    def test_read_Author(self):
        sdist = self._makeOne()
        sdist.read('Author: J. Phredd Bloggs')
        self.assertEqual(sdist.author, 'J. Phredd Bloggs')

    def test_read_Author_Email(self):
        sdist = self._makeOne()
        sdist.read('Author-email: phreddy@example.com')
        self.assertEqual(sdist.author_email, 'phreddy@example.com')

    def test_read_License(self):
        sdist = self._makeOne()
        sdist.read('License: Poetic')
        self.assertEqual(sdist.license, 'Poetic')

    def test_read_Classifier_single(self):
        sdist = self._makeOne()
        sdist.read('Classifier: Some :: Silly Thing')
        self.assertEqual(list(sdist.classifiers), ['Some :: Silly Thing'])

    def test_read_Classifier_multiple(self):
        sdist = self._makeOne()
        sdist.read('Classifier: Some :: Silly Thing\n'
                   'Classifier: Or :: Other')
        self.assertEqual(list(sdist.classifiers),
                         ['Some :: Silly Thing', 'Or :: Other'])

    def test_read_Requires_single_wo_version(self):
        sdist = self._makeOne()
        sdist.read('Requires: SpanishInquisition')
        self.assertEqual(list(sdist.requires), ['SpanishInquisition'])

    def test_read_Requires_single_w_version(self):
        sdist = self._makeOne()
        sdist.read('Requires: SpanishInquisition (>=1.3)')
        self.assertEqual(list(sdist.requires), ['SpanishInquisition (>=1.3)'])

    def test_read_Requires_multiple(self):
        sdist = self._makeOne()
        sdist.read('Requires: SpanishInquisition\n'
                   'Requires: SillyWalks (1.4)\n'
                   'Requires: kniggits (>=2.3,<3.0)')
        self.assertEqual(list(sdist.requires),
                         ['SpanishInquisition',
                          'SillyWalks (1.4)',
                          'kniggits (>=2.3,<3.0)',
                         ])

    def test_read_Provides_single_wo_version(self):
        sdist = self._makeOne()
        sdist.read('Provides: SillyWalks')
        self.assertEqual(list(sdist.provides), ['SillyWalks'])

    def test_read_Provides_single_w_version(self):
        sdist = self._makeOne()
        sdist.read('Provides: SillyWalks (1.4)')
        self.assertEqual(list(sdist.provides), ['SillyWalks (1.4)'])

    def test_read_Provides_multiple(self):
        sdist = self._makeOne()
        sdist.read('Provides: SillyWalks\n'
                   'Provides: DeadlyJoke (3.1.4)')
        self.assertEqual(list(sdist.provides),
                         ['SillyWalks',
                          'DeadlyJoke (3.1.4)',
                         ])

    def test_read_Obsoletes_single_no_version(self):
        sdist = self._makeOne()
        sdist.read('Obsoletes: SillyWalks')
        self.assertEqual(list(sdist.obsoletes), ['SillyWalks'])

    def test_read_Obsoletes_single_w_version(self):
        sdist = self._makeOne()
        sdist.read('Obsoletes: SillyWalks (<=1.3)')
        self.assertEqual(list(sdist.obsoletes), ['SillyWalks (<=1.3)'])

    def test_read_Obsoletes_multiple(self):
        sdist = self._makeOne()
        sdist.read('Obsoletes: kniggits\n'
                   'Obsoletes: SillyWalks (<=2.0)')
        self.assertEqual(list(sdist.obsoletes),
                         ['kniggits',
                          'SillyWalks (<=2.0)',
                         ])
