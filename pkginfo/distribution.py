import rfc822
import StringIO

HEADER_ATTRS = (
    ('Metadata-Version', 'metadata_version', False),
    ('Name', 'name', False),
    ('Version', 'version', False),
    ('Platform', 'platforms', True),
    ('Supported-Platform', 'supported_platforms', True),
    ('Summary', 'summary', False),
    ('Description', 'description', False),
    ('Keywords', 'keywords', False),
    ('Home-Page', 'home_page', False),
    ('Download-URL', 'download_url', False),
    ('Author', 'author', False),
    ('Author-email', 'author_email', False),
    ('License', 'license', False),
    ('Classifier', 'classifiers', True),
    ('Requires', 'requires', True),
    ('Provides', 'provides', True),
    ('Obsoletes', 'obsoletes', True),
)

class Distribution:
    metadata_version = None
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
    classifiers = ()
    requires = ()
    provides = ()
    obsoletes = ()

    def extractMetadata(self):
        data = self.read()
        self.parse(data)

    def read(self):
        raise NotImplementedError

    def parse(self, data):
        fp = StringIO.StringIO(data)
        message = rfc822.Message(fp)

        for header_name, attr_name, multiple in HEADER_ATTRS:
            if header_name in message:
                if multiple:
                    values = message.getheaders(header_name)
                    setattr(self, attr_name, values)
                else:
                    value = message.getheader(header_name)
                    if value != 'UNKNOWN':
                        setattr(self, attr_name, value)
