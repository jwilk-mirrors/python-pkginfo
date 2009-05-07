import unittest

class BDistTests(unittest.TestCase):

    def _getTargetClass(self):
        from pkginfo.bdist import BDist
        return BDist

    def _makeOne(self, filename=None):
        return self._getTargetClass()(filename)

    def _checkSample(self, bdist, filename):
        self.assertEqual(bdist.filename, filename)
        self.assertEqual(bdist.metadata_version, '1.0')
        self.assertEqual(bdist.name, 'mypackage')
        self.assertEqual(bdist.version, '0.1')
        self.assertEqual(bdist.keywords, None)
        self.assertEqual(list(bdist.classifiers),
                         ['Development Status :: 4 - Beta',
                          'Environment :: Console (Text Based)',
                         ])
        self.assertEqual(list(bdist.supported_platforms), [])

    def test_ctor_w_egg(self):
        import os
        d, _ = os.path.split(__file__)
        filename = '%s/../../docs/examples/mypackage-0.1-py2.6.egg' % d
        bdist = self._makeOne(filename)
        self._checkSample(bdist, filename)
