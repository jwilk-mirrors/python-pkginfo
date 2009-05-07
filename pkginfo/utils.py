import os
from types import ModuleType

from pkginfo.bdist import BDist
from pkginfo.develop import Develop
from pkginfo.distribution import Distribution
from pkginfo.installed import Installed
from pkginfo.sdist import SDist

def get_metadata(path_or_module):
    """ Try to create a Distribution 'path_or_module'.
    
    o 'path_or_module' may be a module object.

    o If a string, 'path_or_module' may point to an sdist file, a bdist
      file, an installed package, or a working checkout (if it contains
      PKG-INFO).
    
    o Return None if 'path_or_module' can't be parsed.
    """
    if isinstance(path_or_module, ModuleType):
        try:
            return Installed(path_or_module)
        except (ValueError, IOError):
            pass

    try:
        __import__(path_or_module)
    except ImportError:
        pass
    else:
        try:
            return Installed(path_or_module)
        except (ValueError, IOError):
            pass

    if os.path.isfile(path_or_module):
        try:
            return SDist(path_or_module)
        except (ValueError, IOError):
            pass

        try:
            return BDist(path_or_module)
        except (ValueError, IOError):
            pass

    if os.path.isdir(path_or_module):
        try:
            return Develop(path_or_module)
        except (ValueError, IOError):
            pass
