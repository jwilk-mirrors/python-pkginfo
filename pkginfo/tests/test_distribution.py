import unittest

class DistributionTests(unittest.TestCase):

    def _getTargetClass(self):
        from pkginfo.distribution import Distribution
        return Distribution

    def _makeOne(self):
        return self._getTargetClass()()

    def test_ctor_defaults(self):
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

    def test_parse_Metadata_Version(self):
        dist = self._makeOne()
        dist.parse('Metadata-Version: 1.3')
        self.assertEqual(dist.metadata_version, '1.3')

    def test_parse_Name(self):
        dist = self._makeOne()
        dist.parse('Name: foobar')
        self.assertEqual(dist.name, 'foobar')

    def test_parse_Version(self):
        dist = self._makeOne()
        dist.parse('Version: 2.1.3b5')
        self.assertEqual(dist.version, '2.1.3b5')

    def test_parse_Platform_single(self):
        dist = self._makeOne()
        dist.parse('Platform: Plan9')
        self.assertEqual(list(dist.platforms), ['Plan9'])

    def test_parse_Platform_multiple(self):
        dist = self._makeOne()
        dist.parse('Platform: Plan9\nPlatform: AIX')
        self.assertEqual(list(dist.platforms), ['Plan9', 'AIX'])

    def test_parse_Supported_Platform_single(self):
        dist = self._makeOne()
        dist.parse('Supported-Platform: Plan9')
        self.assertEqual(list(dist.supported_platforms), ['Plan9'])

    def test_parse_Supported_Platform_multiple(self):
        dist = self._makeOne()
        dist.parse('Supported-Platform: i386-win32\n'
                   'Supported-Platform: RedHat 7.2')
        self.assertEqual(list(dist.supported_platforms),
                        ['i386-win32', 'RedHat 7.2'])

    def test_parse_Summary(self):
        dist = self._makeOne()
        dist.parse('Summary: Package for foo')
        self.assertEqual(dist.summary, 'Package for foo')

    def test_parse_Description(self):
        dist = self._makeOne()
        dist.parse('Description: This package enables integration with\n'
                   '       foo servers.')
        self.assertEqual(dist.description,
                         'This package enables integration with\n'
                         ' foo servers.')

    def test_parse_Keywords(self):
        dist = self._makeOne()
        dist.parse('Keywords: bar foo qux')
        self.assertEqual(dist.keywords, 'bar foo qux')

    def test_parse_Home_page(self):
        dist = self._makeOne()
        dist.parse('Home-page: http://example.com/package')
        self.assertEqual(dist.home_page, 'http://example.com/package')

    def test_parse_Download_URL(self):
        dist = self._makeOne()
        dist.parse('Download-URL: '
                   'http://example.com/package/mypackage-0.1.zip')
        self.assertEqual(dist.download_url,
                         'http://example.com/package/mypackage-0.1.zip')

    def test_parse_Author(self):
        dist = self._makeOne()
        dist.parse('Author: J. Phredd Bloggs')
        self.assertEqual(dist.author, 'J. Phredd Bloggs')

    def test_parse_Author_Email(self):
        dist = self._makeOne()
        dist.parse('Author-email: phreddy@example.com')
        self.assertEqual(dist.author_email, 'phreddy@example.com')

    def test_parse_License(self):
        dist = self._makeOne()
        dist.parse('License: Poetic')
        self.assertEqual(dist.license, 'Poetic')

    def test_parse_Classifier_single(self):
        dist = self._makeOne()
        dist.parse('Classifier: Some :: Silly Thing')
        self.assertEqual(list(dist.classifiers), ['Some :: Silly Thing'])

    def test_parse_Classifier_multiple(self):
        dist = self._makeOne()
        dist.parse('Classifier: Some :: Silly Thing\n'
                   'Classifier: Or :: Other')
        self.assertEqual(list(dist.classifiers),
                         ['Some :: Silly Thing', 'Or :: Other'])

    def test_parse_Requires_single_wo_version(self):
        dist = self._makeOne()
        dist.parse('Requires: SpanishInquisition')
        self.assertEqual(list(dist.requires), ['SpanishInquisition'])

    def test_parse_Requires_single_w_version(self):
        dist = self._makeOne()
        dist.parse('Requires: SpanishInquisition (>=1.3)')
        self.assertEqual(list(dist.requires), ['SpanishInquisition (>=1.3)'])

    def test_parse_Requires_multiple(self):
        dist = self._makeOne()
        dist.parse('Requires: SpanishInquisition\n'
                   'Requires: SillyWalks (1.4)\n'
                   'Requires: kniggits (>=2.3,<3.0)')
        self.assertEqual(list(dist.requires),
                         ['SpanishInquisition',
                          'SillyWalks (1.4)',
                          'kniggits (>=2.3,<3.0)',
                         ])

    def test_parse_Provides_single_wo_version(self):
        dist = self._makeOne()
        dist.parse('Provides: SillyWalks')
        self.assertEqual(list(dist.provides), ['SillyWalks'])

    def test_parse_Provides_single_w_version(self):
        dist = self._makeOne()
        dist.parse('Provides: SillyWalks (1.4)')
        self.assertEqual(list(dist.provides), ['SillyWalks (1.4)'])

    def test_parse_Provides_multiple(self):
        dist = self._makeOne()
        dist.parse('Provides: SillyWalks\n'
                   'Provides: DeadlyJoke (3.1.4)')
        self.assertEqual(list(dist.provides),
                         ['SillyWalks',
                          'DeadlyJoke (3.1.4)',
                         ])

    def test_parse_Obsoletes_single_no_version(self):
        dist = self._makeOne()
        dist.parse('Obsoletes: SillyWalks')
        self.assertEqual(list(dist.obsoletes), ['SillyWalks'])

    def test_parse_Obsoletes_single_w_version(self):
        dist = self._makeOne()
        dist.parse('Obsoletes: SillyWalks (<=1.3)')
        self.assertEqual(list(dist.obsoletes), ['SillyWalks (<=1.3)'])

    def test_parse_Obsoletes_multiple(self):
        dist = self._makeOne()
        dist.parse('Obsoletes: kniggits\n'
                   'Obsoletes: SillyWalks (<=2.0)')
        self.assertEqual(list(dist.obsoletes),
                         ['kniggits',
                          'SillyWalks (<=2.0)',
                         ])
