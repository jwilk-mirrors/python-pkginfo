import unittest

class InstalledTests(unittest.TestCase):

    def _getTargetClass(self):
        from pkginfo.installed import Installed
        return Installed

    def _makeOne(self, filename=None):
        return self._getTargetClass()(filename)

    def test_ctor_w_package(self):
        import pkginfo
        from pkginfo.tests import _checkSample
        installed = self._makeOne(pkginfo)
        self.assertEqual(installed.package.__name__, 'pkginfo')
        _checkSample(self, installed)

    def test_ctor_w_name(self):
        from pkginfo.tests import _checkSample
        installed = self._makeOne('pkginfo')
        self.assertEqual(installed.package.__name__, 'pkginfo')
        _checkSample(self, installed)
