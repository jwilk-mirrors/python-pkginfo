import unittest

class InstalledTests(unittest.TestCase):

    def _getTargetClass(self):
        from pkginfo.installed import Installed
        return Installed

    def _makeOne(self, filename=None):
        return self._getTargetClass()(filename)

    def _checkSample(self, installed):
        self.assertEqual(installed.package.__name__, 'pkginfo')
        self.assertEqual(installed.metadata_version, '1.0')
        self.assertEqual(installed.name, 'pkginfo')
        self.assertEqual(installed.version, '0.1')
        self.assertEqual(installed.keywords,
                         'distribution sdist installed metadata' )
        self.assertEqual(list(installed.classifiers), [])
        self.assertEqual(list(installed.supported_platforms), [])

    def test_ctor_w_package(self):
        import pkginfo
        installed = self._makeOne(pkginfo)
        self._checkSample(installed)

    def test_ctor_w_name(self):
        installed = self._makeOne('pkginfo')
        self._checkSample(installed)
