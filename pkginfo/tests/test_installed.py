import unittest

class InstalledTests(unittest.TestCase):

    def _getTargetClass(self):
        from pkginfo.installed import Installed
        return Installed

    def _makeOne(self, filename=None, metadata_version=None):
        if metadata_version is not None:
            return self._getTargetClass()(filename, metadata_version)
        return self._getTargetClass()(filename)

    def test_ctor_w_package(self):
        import pkginfo
        from pkginfo.tests import _checkSample
        installed = self._makeOne(pkginfo)
        self.assertEqual(installed.metadata_version, '1.0')
        self.assertEqual(installed.package.__name__, 'pkginfo')
        _checkSample(self, installed)

    def test_ctor_w_package_and_metadata_version(self):
        import pkginfo
        from pkginfo.tests import _checkSample
        installed = self._makeOne(pkginfo, metadata_version='1.2')
        self.assertEqual(installed.metadata_version, '1.2')
        self.assertEqual(installed.package.__name__, 'pkginfo')
        _checkSample(self, installed)

    def test_ctor_w_name(self):
        from pkginfo.tests import _checkSample
        installed = self._makeOne('pkginfo')
        self.assertEqual(installed.metadata_version, '1.0')
        self.assertEqual(installed.package.__name__, 'pkginfo')
        _checkSample(self, installed)

    def test_ctor_w_name_and_metadata_version(self):
        from pkginfo.tests import _checkSample
        installed = self._makeOne('pkginfo', metadata_version='1.2')
        self.assertEqual(installed.metadata_version, '1.2')
        self.assertEqual(installed.package.__name__, 'pkginfo')
        _checkSample(self, installed)
