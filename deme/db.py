import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Called when the application has been created and is handling a request.
    """

    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """
    Checks if a connection was created. If the connection exists, it is closed.
    """

    db = g.pop("db", None)

    if db is not None:
        db.close()
