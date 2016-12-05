import sys
from optparse import OptionParser

from .write import write_text, get_root_date

def print_usage():
    print("Usage: vanity [command]")
    print("")
    print("commands:")
    print("  help   show this help message and exit")
    print("  write  write your vanity text to a git repo")


def write():
    usage = "usage: vanity write [options] text repo_path"
    parser = OptionParser(usage=usage)

    default_start_date = get_root_date()

    parser.add_option("--offset", dest="offset",
                      help="number of spaces to leave to the left (default is 0)",
                      default=0)

    parser.add_option("--spacing", dest="spacing",
                      help="spacing between letters (default is 1)",
                      default=1)

    parser.add_option("--space-width", dest="space_width",
                      help="width of space character (default is 4)",
                      default=4)

    parser.add_option("--commits", dest="offset",
                      help="number of commits per pixel (default is 50)",
                      default=50)

    parser.add_option("--start_date", dest="start_date",
                      help="the date of the first commit, should be a Sunday "
                           "(default is %s)" % default_start_date,
                      default=default_start_date)


    (options, args) = parser.parse_args()

    print options
    print args



def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command == 'write':
        write()
        return

    print_usage()

