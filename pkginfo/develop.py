import glob
import os
import sys
import warnings

from pkginfo.distribution import Distribution

class Develop(Distribution):

    def __init__(self, path):
        self.path = os.path.abspath(
                        os.path.normpath(
                            os.path.expanduser(path)))
        self.extractMetadata()

    def read(self):
        candidates = [self.path]
        candidates.extend(glob.glob(os.path.join(self.path, '*.egg-info')))
        candidates.extend(glob.glob(os.path.join(self.path, 'EGG-INFO')))
        for candidate in candidates:
            if os.path.isdir(candidate):
                path = os.path.join(candidate, 'PKG-INFO')
                if os.path.exists(path):
                    return open(path).read()
        warnings.warn('No PKG-INFO found for path: %s' % self.path)
