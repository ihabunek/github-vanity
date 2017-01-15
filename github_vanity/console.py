import os
import sys

from datetime import datetime
from git import Repo
from git.exc import InvalidGitRepositoryError
from optparse import OptionParser

from .write import write_text, get_root_date


def print_usage():
    print("Usage: vanity [command]")
    print("")
    print("https://github.com/ihabunek/github-vanity")
    print("")
    print("commands:")
    print("  help   show this help message and exit")
    print("  write  write your vanity text to a git repo")


def print_err(msg):
    sys.stderr.write('\033[91m' + msg + '\033[0m' + "\n")


def parse_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None


def write():
    usage = (
        "vanity write [options] TEXT"
        "\n\nhttps://github.com/ihabunek/github-vanity"
    )

    parser = OptionParser(usage=usage)

    default_start_date = str(get_root_date())

    parser.add_option("-d", "--start_date", dest="start_date", type="string",
                      help="the date of the first commit, should be a Sunday "
                           "(default is 53 weeks ago, which targets the leftmost "
                           "pixel in the GitHub activity chart i.e. %s)" % default_start_date,
                      default=default_start_date)

    parser.add_option("-o", "--offset", dest="offset", type="int",
                      help="number of spaces to leave to the left (default is 0)",
                      default=0)

    parser.add_option("-s", "--spacing", dest="spacing", type="int",
                      help="spacing between letters (default is 1)",
                      default=1)

    parser.add_option("-w", "--space-width", dest="space_width", type="int",
                      help="width of space character (default is 4)",
                      default=4)

    parser.add_option("-c", "--commits", dest="commits", type="int",
                      help="number of commits per pixel (default is 50)",
                      default=50)

    (options, args) = parser.parse_args()

    options.start_date = parse_date(options.start_date)
    if not options.start_date:
        parser.error("option --start-date: invalid date (YYYY-MM-DD)")

    if len(args) < 2:
        parser.print_help()
        return

    try:
        repo = Repo(os.getcwd())
    except InvalidGitRepositoryError:
        print_err("This is not a valid Git repository")
        return

    text = args[1].lower()

    write_text(text, repo, **options.__dict__)


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command == 'write':
        write()
        return

    print_usage()
