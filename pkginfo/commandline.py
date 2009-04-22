import optparse
from pkginfo import get_metadata
from pkginfo.distribution import HEADER_ATTRS

_usage = """Print the metadata for a python package zip, egg or directory.
If no options are given, a human readable version of all the metadata
is printed to stdout.

If any attribute options are given, only the named attributes are printed
as a semicolon separated list of values. Keys are not shown.

The delimiter can be changed with the --delim option.
"""

def _parse_options():
    parser = optparse.OptionParser(usage=_usage)

    parser.add_option("-d", "--delim", dest="delim", default=";",
                      help="Delimit fields with this DELIM", metavar="DELIM")
    for name, attr, flag in HEADER_ATTRS:
        parser.add_option("--%s" % attr,
                          help="Add %s to list of fields to show" % name.lower(),
                          dest="showattrs", action="append_const", const=attr )

    options, args = parser.parse_args()
    if len(args)==0:
        parser.error("command takes a one or more file or directory as argument")
    else:
        return options, args

def _print_human_readable(meta):
    """print lines of  "key: value" to stdout. values that are null or
    an empty tuple are ignored"""
    for name in meta:
        value = getattr(meta, name)
        if value is not None and value!=():
            print "%s: %s" % (name, value)

def _print_attributes(meta, attrs, delim):
    values=[getattr(meta, e) for e in attrs]
    print delim.join(values)
                
def main():
    """Entry point for pkginfo tool"""
    options, paths = _parse_options()

    for path in paths:
        meta = get_metadata(path)
        if meta is None:
            continue

        if options.showattrs:
            _print_attributes(meta, options.showattrs, options.delim)
        else:
            _print_human_readable(meta)

    
