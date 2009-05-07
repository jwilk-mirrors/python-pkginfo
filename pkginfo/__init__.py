import os
from pkginfo.bdist import BDist
from pkginfo.distribution import Distribution
from pkginfo.installed import Installed
from pkginfo.sdist import SDist

__all__ = ["BDist", "SDist", "Installed", "get_metadata"]
__version__ = "0.3"

def get_metadata(path):
    """Try to get metadata from path, which may be an sdist, bdist or
    installed package. If it's not possible to parse as either, returns
    None"""
    try:
        return BDist(path)
    except (ValueError, IOError):
        pass

    try:
        return SDist(path)
    except (ValueError, IOError):
        pass

    if not os.path.exists: # installed backage can't be a file
        try:
            return Installed(path)
        except (ValueError, IOError):
            pass

    return None



