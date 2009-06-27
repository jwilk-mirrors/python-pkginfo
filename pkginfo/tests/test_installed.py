import unittest

import sys

if sys.version_info >= (2, 6):  # no PKG-INFO installed in earlier Pythons

    class InstalledTests(unittest.TestCase):

        def _getTargetClass(self):
            from pkginfo.installed import Installed
            return Installed

        def _makeOne(self, filename=None, metadata_version=None):
            if metadata_version is not None:
                return self._getTargetClass()(filename, metadata_version)
            return self._getTargetClass()(filename)

        def test_ctor_w_package_no___file__(self):
            import sys
            import warnings
            old_filters = warnings.filters[:]
            warnings.filterwarnings('ignore')
            try:
                installed = self._makeOne(sys)
                self.assertEqual(installed.package, sys)
                self.assertEqual(installed.package_name, 'sys')
                self.assertEqual(installed.metadata_version, None)
            finally:
                warnings.filters[:] = old_filters

        def test_ctor_w_package(self):
            import pkginfo
            from pkginfo.tests import _checkSample
            installed = self._makeOne(pkginfo)
            self.assertEqual(installed.package, pkginfo)
            self.assertEqual(installed.package_name, 'pkginfo')
            self.assertEqual(installed.metadata_version, '1.0')
            _checkSample(self, installed)

        def test_ctor_w_package_no_PKG_INFO(self):
            import types
            import warnings
            from pkginfo.tests import _checkSample
            old_filters = warnings.filters[:]
            warnings.filterwarnings('ignore')
            try:
                installed = self._makeOne(types)
                self.assertEqual(installed.package, types)
                self.assertEqual(installed.package_name, 'types')
                self.assertEqual(installed.metadata_version, None)
            finally:
                warnings.filters[:] = old_filters

        def test_ctor_w_package_and_metadata_version(self):
            import pkginfo
            from pkginfo.tests import _checkSample
            installed = self._makeOne(pkginfo, metadata_version='1.2')
            self.assertEqual(installed.metadata_version, '1.2')
            self.assertEqual(installed.package.__name__, 'pkginfo')
            _checkSample(self, installed)

        def test_ctor_w_name(self):
            import pkginfo
            from pkginfo.tests import _checkSample
            installed = self._makeOne('pkginfo')
            self.assertEqual(installed.metadata_version, '1.0')
            self.assertEqual(installed.package, pkginfo)
            self.assertEqual(installed.package_name, 'pkginfo')
            _checkSample(self, installed)

        def test_ctor_w_name_and_metadata_version(self):
            import pkginfo
            from pkginfo.tests import _checkSample
            installed = self._makeOne('pkginfo', metadata_version='1.2')
            self.assertEqual(installed.metadata_version, '1.2')
            self.assertEqual(installed.package, pkginfo)
            self.assertEqual(installed.package_name, 'pkginfo')
            _checkSample(self, installed)

        def test_ctor_w_invalid_name(self):
            installed = self._makeOne('nonesuch')
            self.assertEqual(installed.package, None)
            self.assertEqual(installed.package_name, 'nonesuch')
            self.assertEqual(installed.metadata_version, None)

