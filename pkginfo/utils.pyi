import types

from .bdist import BDist as BDist
from .develop import Develop as Develop
from .installed import Installed as Installed
from .sdist import SDist as SDist
from .wheel import Wheel as Wheel

def get_metadata(path_or_module: str | types.ModuleType, metadata_version: str | None = ...): ...
