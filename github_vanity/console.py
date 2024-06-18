import os
import sys
from argparse import ArgumentParser, Namespace
from datetime import date, datetime
from typing import List

from git import Repo
from git.exc import InvalidGitRepositoryError, NoSuchPathError

from github_vanity import ConsoleError
from github_vanity.font import font as chars
from github_vanity.font import get_char_grid
from github_vanity.utils import batched

from .write import get_root_date, write_text


def print_err(msg: str):
    sys.stderr.write("\033[91m" + msg + "\033[0m" + "\n")


def parse_date(date: str) -> date:
    return datetime.strptime(date, "%Y-%m-%d").date()


def make_parser():
    parser = ArgumentParser(
        description="Write to your Github activity chart",
        epilog="https://github.com/ihabunek/github-vanity",
    )

    subparsers = parser.add_subparsers(required=True)

    font_parser = subparsers.add_parser("font", help="Show available font characters")
    font_parser.set_defaults(func=font)

    preview_parser = subparsers.add_parser(
        "preview", help="Preview how the text will appear in the chart"
    )
    preview_parser.set_defaults(func=preview)
    preview_parser.add_argument("text", help="Text to preview")

    preview_parser.add_argument(
        "-s",
        "--spacing",
        type=int,
        help="spacing between letters (default: %(default)s)",
        default=1,
    )

    write_parser = subparsers.add_parser("write", help="Write to repo")
    write_parser.set_defaults(func=write)
    write_parser.add_argument("text", help="Text to write to chart")

    write_parser.add_argument(
        "-r",
        "--repo",
        help="Path to the git repository (defaults to current dir)",
        default=os.getcwd(),
    )

    write_parser.add_argument(
        "-d",
        "--start_date",
        type=parse_date,
        help="""date of the first commit, should be a Sunday (default is 53
        weeks ago, which targets the leftmost pixel in the GitHub activity
        chart i.e. %(default)s)""",
        default=get_root_date(),
    )

    write_parser.add_argument(
        "-o",
        "--offset",
        type=int,
        help="number of spaces to leave to the left (default: %(default)s)",
        default=0,
    )

    write_parser.add_argument(
        "-s",
        "--spacing",
        type=int,
        help="spacing between letters (default: %(default)s)",
        default=1,
    )

    write_parser.add_argument(
        "-w",
        "--space-width",
        type=int,
        help="width of space character (default: %(default)s)",
        default=4,
    )

    write_parser.add_argument(
        "-c",
        "--commits",
        type=int,
        help="number of commits per pixel (default: %(default)s)",
        default=50,
    )

    return parser


def get_repo(path: str):
    try:
        return Repo(path)
    except NoSuchPathError:
        raise ConsoleError("Given path does not exist: {}".format(path))
    except InvalidGitRepositoryError:
        raise ConsoleError("This is not a valid Git repository")


def main():
    parser = make_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except ConsoleError as ex:
        print_err(str(ex))
        return 1


def write(args: Namespace):
    repo = get_repo(args.repo)
    print(f"Found repo at {repo.git_dir}")

    # Warn if repo is not empty
    is_empty = repo.head.is_detached and len(repo.refs) == 0
    if not is_empty:
        val = input("Repo is not empty. Continue? [y/N]: ")
        if val.strip().lower() != "y":
            print("Aborted")
            return

    write_text(
        repo,
        args.text.lower(),
        start_date=args.start_date,
        offset=args.offset,
        spacing=args.spacing,
        space_width=args.space_width,
        commits=args.commits,
    )


def font(_: Namespace):
    for grid in chars.values():
        for row in grid:
            print(row)


def preview(args: Namespace):
    grids = [get_char_grid(char) for char in args.text]
    space = " " * args.spacing
    joined = [space.join(grid[y] for grid in grids) for y in range(7)]
    print_halfblock(joined)


def print_halfblock(grid: List[str]):
    def _gen(pairs):
        yield "\033[92m"  # green foreground

        for top, bottom in pairs:
            if top == " " and bottom == " ":
                yield " "
            elif top == " ":
                yield "\N{LOWER HALF BLOCK}"
            elif bottom == " ":
                yield "\N{UPPER HALF BLOCK}"
            else:
                yield "\N{FULL BLOCK}"

        yield "\033[0m"  # reset ansi

    for row in batched(grid, 2):
        # Handle last row by adding a blank row below
        if len(row) == 1:
            pairs = zip(row[0], " " * len(row[0]))
        else:
            pairs = zip(row[0], row[1])

        print("".join(_gen(pairs)))
