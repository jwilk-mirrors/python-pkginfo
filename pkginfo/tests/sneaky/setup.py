from setuptools import setup, find_packages

setup(
    name='namespaced.sneaky',
    version='0.1',
    description='Test namespaced packages with non-root egg-info.',
    author='Tres Seaver',
    author_email='tseaver@palladion.com',
    long_description='Blah, blah.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['namespaced',],
    install_requires=['setuptools'],
    zip_safe=False,
)
