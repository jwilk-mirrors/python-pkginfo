from .distribution import Distribution as Distribution

class Index(dict):
    def __setitem__(self, key: str, value: Distribution) -> None: ...
    def add(self, distribution: Distribution) -> None: ...
