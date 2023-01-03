from typing import Callable
from typing import Generator
from typing import Sequence
from typing import Tuple

def parse(fp): ...
def get(msg, header): ...
def get_all(msg, header): ...

_header_attr_triple = Tuple[str, str, bool]
_header_attrs = Tuple[_header_attr_triple]
HEADER_ATTRS_1_0: _header_attrs
HEADER_ATTRS_1_1: _header_attrs
HEADER_ATTRS_1_2: _header_attrs
HEADER_ATTRS_2_0 = HEADER_ATTRS_1_2
HEADER_ATTRS_2_1: _header_attrs
HEADER_ATTRS_2_2: _header_attrs
HEADER_ATTRS: _header_attrs

class Distribution:
    metadata_version: str
    name: str
    version: str
    platforms: Sequence[str]
    supported_platforms: Sequence[str]
    summary: str
    description: str
    keywords: str
    home_page: str
    download_url: str
    author: str
    author_email: str
    license: str
    classifiers: Sequence[str]
    requires: Sequence[str]
    provides: Sequence[str]
    obsoletes: Sequence[str]
    maintainer: str
    maintainer_email: str
    requires_python: str
    requires_external: Sequence[str]
    requires_dist: Sequence[str]
    provides_dist: Sequence[str]
    obsoletes_dist: Sequence[str]
    project_urls: Sequence[str]
    provides_extras: Sequence[str]
    description_content_type: str
    dynamic: Sequence[str]
    def extractMetadata(self) -> None: ...
    def read(self) -> None: ...
    def parse(self, data) -> None: ...
    def __iter__(self) -> Generator[str, None, None]: ...
    iterkeys: Generator[str, None, None]
