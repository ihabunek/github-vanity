======================
Vanity text for GitHub
======================

Write to your GitHub activity chart.

Inspired by `Rockstar <https://github.com/avinassh/rockstar/>`_

.. image:: https://img.shields.io/pypi/v/github-vanity.svg?style=flat-square
  :target: https://pypi.org/project/github-vanity/

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
  :target: LICENSE

.. image:: https://img.shields.io/badge/author-%40ihabunek-blue.svg?style=flat-square
  :target: https://twitter.com/ihabunek

Installation
------------

From Python Package Index
~~~~~~~~~~~~~~~~~~~~~~~~~

Preferably install into a virtual environment.

.. code-block:: bash

    pip install github-vanity

Usage
-----

Initialize an empty Git repository which you will submit to GitHub.

Populate the repo with the desired text:

.. code-block:: bash

    vanity write "Hi there!"

Push the repo to GitHub and presto!

.. image:: https://raw.githubusercontent.com/ihabunek/github-vanity/master/vanity.jpg

Reference
---------

``vanity write [options] text``

- **text** - text to write to the commit chart

Available options:

- **-h**, **--help** - show usage instructions
- **-d**, **--start_date** - the date to start with, **should be a Sunday**
- **-o**, **--offset** - number of spaces to leave to the left (default is 0)
- **-s**, **--spacing** - spacing between letters (default is 1)
- **-w**, **--space_width** - width of space character (default is 4)
- **-c**, **--commits** - number of commits per pixel (default is 50)
- **-r**, **--repo** - path to the git repo to modify (defaults to current dir)

The default ``start_date`` is the Sunday 52 weeks before the last one, which
is the first pixel visible on the commit chart.

