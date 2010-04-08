import rfc822
import StringIO

HEADER_ATTRS_1_0 = ( # PEP 241
    ('Metadata-Version', 'metadata_version', False),
    ('Name', 'name', False),
    ('Version', 'version', False),
    ('Platform', 'platforms', True),
    ('Supported-Platform', 'supported_platforms', True),
    ('Summary', 'summary', False),
    ('Description', 'description', False),
    ('Keywords', 'keywords', False),
    ('Home-Page', 'home_page', False),
    ('Author', 'author', False),
    ('Author-email', 'author_email', False),
    ('License', 'license', False),
)

HEADER_ATTRS_1_1 = HEADER_ATTRS_1_0 + ( # PEP 314
    ('Classifier', 'classifiers', True),
    ('Download-URL', 'download_url', False),
    ('Requires', 'requires', True),
    ('Provides', 'provides', True),
    ('Obsoletes', 'obsoletes', True),
)

HEADER_ATTRS_1_2 = HEADER_ATTRS_1_1 + ( # PEP 345
    ('Maintainer', 'maintainer', False),
    ('Maintainer-email', 'maintainer_email', False),
    ('Requires-Python', 'requires_python', False),
    ('Requires-External', 'requires_external', True),
    ('Requires-Dist', 'requires_dist', True),
    ('Provides-Dist', 'provides_dist', True),
    ('Obsoletes-Dist', 'obsoletes_dist', True),
    ('Project-URL', 'project_urls', True),
)

HEADER_ATTRS = {
    '1.0': HEADER_ATTRS_1_0,
    '1.1': HEADER_ATTRS_1_1,
    '1.2': HEADER_ATTRS_1_2,
}

class Distribution(object):
    metadata_version = None
    # version 1.0
    name = None
    version = None
    platforms = ()
    supported_platforms = ()
    summary = None
    description = None
    keywords = None
    home_page = None
    download_url = None
    author = None
    author_email = None
    license = None
    # version 1.1
    classifiers = ()
    requires = ()
    provides = ()
    obsoletes = ()
    # version 1.2
    maintainer = None
    maintainer_email = None
    requires_python = None
    requires_external = ()
    requires_dist = ()
    provides_dist = ()
    obsoletes_dist = ()
    project_urls = ()

    def extractMetadata(self):
        data = self.read()
        self.parse(data)

    def read(self):
        raise NotImplementedError

    def _getHeaderAttrs(self):
        return HEADER_ATTRS.get(self.metadata_version, [])

    def parse(self, data):
        fp = StringIO.StringIO(data)
        message = rfc822.Message(fp)

        if 'Metadata-Version' in message and self.metadata_version is None:
            value = message.getheader('Metadata-Version')
            metadata_version = self.metadata_version = value

        for header_name, attr_name, multiple in self._getHeaderAttrs():

            if attr_name == 'metadata_version':
                continue

            if header_name in message:
                if multiple:
                    values = message.getheaders(header_name)
                    setattr(self, attr_name, values)
                else:
                    value = message.getheader(header_name)
                    if value != 'UNKNOWN':
                        setattr(self, attr_name, value)
                        
    def __iter__(self):
        for header_name, attr_name, multiple in self._getHeaderAttrs():
            yield attr_name

    iterkeys = __iter__
 
