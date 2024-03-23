import io
import os
import pathlib
import tarfile
import zipfile

from .distribution import Distribution

class SDist(Distribution):

    def __init__(self, filename, metadata_version=None):
        self.filename = filename
        self.metadata_version = metadata_version
        self.extractMetadata()

    @staticmethod
    def _get_archive(fqp):
        if not fqp.exists():
            raise ValueError('No such file: %s' % fqp)

        if zipfile.is_zipfile(fqp):
            archive = zipfile.ZipFile(fqp)
            names = archive.namelist()
            def read_file(name):
                return archive.read(name)
        elif tarfile.is_tarfile(fqp):
            archive = tarfile.TarFile.open(fqp)
            names = archive.getnames()
            def read_file(name):
                return archive.extractfile(name).read()
        else:
            raise ValueError('Not a known archive format: %s' % fqp)

        return archive, names, read_file


    def read(self):
        fqp = pathlib.Path(self.filename).resolve()

        archive, names, read_file = self._get_archive(fqp)

        try:
            tuples = [x.split('/') for x in names if 'PKG-INFO' in x]
            schwarz = sorted([(len(x), x) for x in tuples])
            for path in [x[1] for x in schwarz]:
                candidate = '/'.join(path)
                data = read_file(candidate)
                if b'Metadata-Version' in data:
                    return data
        finally:
            archive.close()

        raise ValueError('No PKG-INFO in archive: %s' % fqp)


class UnpackedSDist(SDist):
    def __init__(self, filename, metadata_version=None):
        file_path = pathlib.Path(filename)

        if file_path.is_dir():
            pass
        elif file_path.is_file():
            filename = file_path.parent
        else:
            raise ValueError('No such file: %s' % filename)

        super(UnpackedSDist, self).__init__(
                filename, metadata_version=metadata_version)

    def read(self):
        try:
            pkg_info = os.path.join(self.filename, 'PKG-INFO')
            with io.open(pkg_info, errors='ignore') as f:
                return f.read()
        except Exception as e:
            raise ValueError('Could not load %s as an unpacked sdist: %s'
                                % (self.filename, e))
