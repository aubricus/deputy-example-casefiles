"""
Usage: deputy foo [options]

options:
    -x      Do something custom!
"""

from docopt import docopt
from subprocess import call

def run(argv):
    """Foo bar baz qux!"""

    args = docopt(__doc__, argv)

    if args['-x']:
        call(['echo', 'foo bar baz qux!'])
