from datetime import date, timedelta
from sys import stdout
from typing import Optional

from git.repo import Repo

from .font import get_char_grid, get_char_width


def get_root_date():
    """
    Returns the date corresponding to top left pixel on the github chart on the
    current day.
    """
    today = date.today()
    weekday = today.weekday()
    last_sunday = today if weekday == 6 else today - timedelta(days=weekday + 1)
    return last_sunday - timedelta(weeks=52)


def get_date(start_date: date, x: int, y: int) -> date:
    """
    Returns the date correspoinding to (`x`, `y`) coordinates on the chart given
    that `start_date` corresponds to the top left pixel.
    """
    if x < 0 or y < 0 or y > 6:
        raise ValueError("Out of bounds")

    return start_date + timedelta(weeks=x) + timedelta(days=y)


def write_pixel(repo: Repo, start_date: date, x: int, y: int, commits: int):
    date = get_date(start_date, x, y)
    datetime = "%sT12:00:00" % str(date)

    for i in range(commits):
        msg = "Commit lovingly crafted by Github Vanity\n\n"
        msg += "Pixel at (%d, %d), commit %d\n" % (x, y, i)
        msg += "https://github.com/ihabunek/github-vanity"

        repo.index.commit(msg, commit_date=datetime, author_date=datetime)


def write_char(repo: Repo, char: str, start_date: date, offset: int, commits: int):
    grid = get_char_grid(char)
    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            if pixel != " ":
                stdout.write(".")
                stdout.flush()
                write_pixel(repo, start_date, x + offset, y, commits)


def write_text(
    text: str,
    repo: Repo,
    start_date: Optional[date] = None,
    offset: int = 0,
    spacing: int = 1,
    space_width: int = 4,
    commits: int = 50,
):
    if start_date is None:
        start_date = get_root_date()

    for char in text:
        if char == " ":
            offset += space_width
            continue

        width = get_char_width(char)

        print("\nWriting '%s' at offset %d" % (char, offset))
        write_char(repo, char, start_date, offset, commits)

        offset += width + spacing

    print("\nDone")
