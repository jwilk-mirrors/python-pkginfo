import os
import rfc822
import StringIO
import tarfile
import zipfile

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

class SDist:
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

    def __init__(self, filename):
        self.filename = filename
        if filename is not None:
            data = self.extract()
            self.read(data)

    def extract(self):
        fqn = os.path.abspath(
                os.path.normpath(self.filename))
        if not os.path.exists(fqn):
            raise ValueError('No such file: %s' % fqn)

        if fqn.endswith('.zip'):
            archive = zipfile.ZipFile(fqn)
            names = archive.namelist()
            def read_file(name):
                return archive.read(name)
        elif fqn.endswith('.bz2') or fqn.endswith('gz'):
            archive = tarfile.TarFile.open(fqn)
            names = archive.getnames()
            def read_file(name):
                return archive.extractfile(name).read()
        else:
            raise ValueError('Not a known archive format: %s' % fqn)

        tuples = [x.split('/') for x in names if 'PKG-INFO' in x]
        schwarz = sorted([(len(x), x) for x in tuples])
        for path in [x[1] for x in schwarz]:
            candidate = '/'.join(path)
            data = read_file(candidate)
            if 'Metadata-Version' in data:
                return data

        raise ValueError('No PKG-INFO in archive: %s' % fqn)

    def read(self, data):
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
