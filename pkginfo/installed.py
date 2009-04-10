import glob
import os
import sys

from pkginfo.distribution import Distribution

class Installed(Distribution):

    def __init__(self, package):
        if isinstance(package, basestring):
            __import__(package)
            package = sys.modules[package]
        self.package = package
        self.extractMetadata()

    def read(self):
        package = self.package.__package__
        pattern = '%s*.egg-info' % package
        dir, name = os.path.split(self.package.__file__)
        candidates = glob.glob(os.path.join(dir, pattern))
        candidates.extend(glob.glob(os.path.join(dir, '..', pattern)))
        for candidate in candidates:
            if os.path.isdir(candidate):
                path = os.path.join(candidate, 'PKG-INFO')
            else:
                path = candidate
            if os.path.exists(path):
                return open(path).read()
        warnings.warn('No PKG-INFO found for package: %s' % package)
