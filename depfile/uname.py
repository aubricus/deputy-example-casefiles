"""
Usage: deputy uname [options]

options:
    -x      Do something custom!
    -a      Behave as though all of the options -mnrsv were specified.
    -m      print the machine hardware name.
    -n      print the nodename
    -p      print the machine processor architecture name.
    -r      print the operating system release.
    -s      print the operating system name.
    -v      print the operating system version.
"""

from docopt import docopt
from subprocess import call
import sys


def run(argv):
    """Print system information."""

    args = docopt(__doc__, argv)

    # Trivial example:
    # -x is NOT a standard uname option.
    #
    # If: -x is set do custom action.
    # Else: pass argv through.
    if args['-x']:
        sys.exit(call(['uname', '-nmsp']))
    else:
        sys.exit(call(argv))
