from setuptools import setup

NAME = "testlp1974172"
DESCRIPTION = f"""\
Package: {NAME}
==============================

This distribution exists to allow testing wheels with the description
in the "body" of the metadata, rather than in a header.

We make it long enough here, and with enough embeded markup, to try to
trigger that feature during wheel build.

See also:

- https://bugs.launchpad.net/pkginfo/+bug/1885458
- https://peps.python.org/pep-0566/#description
"""

setup(
    name=NAME,
    description="Reproduce LP #1885458",
    long_description=DESCRIPTION,
)
