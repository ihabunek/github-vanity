======================
Vanity text for GitHub
======================

Write to your GitHub activity chart.

Licensed under the MIT License, see `LICENSE <LICENSE>`_.

Usage
-----

Initialize an empty repo which you will submit to GitHub.

Populate the repo like so:

.. code-block:: python

    from git import Repo
    from github_vanity import write_text

    repo = Repo('/path/to/repo/.git')
    write_text("hi there!", repo, offset=7)

Push the repo to GitHub and presto!

.. image:: https://raw.githubusercontent.com/ihabunek/github-vanity/master/vanity.jpg

Reference
---------

``github_vanity.write_text(text, repo, offset, start_date)``

- **text** - the text to write
- **repo** - the repo to write to
- **offset** - number of spaces to leave to the left (default is 0)
- **spacing** - spacing between letters (default is 1)
- **commits** - number of commits per pixel (default is 50)
- **start_date** - the date to start with, should be a Sunday (default start date is the Sunday 52 weeks before the last one, which is the first pixel visible on the chart)


TODO
----

- make a CLI interface
- target a specific branch
- publish to the Cheese shop
