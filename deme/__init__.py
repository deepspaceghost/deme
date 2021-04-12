import os

from flask import Flask


def create_app(test_config=None):
    """
    Create and configure the app.
    """

    app = app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "deme.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/congratulations")
    def congratulations():
        """
        Prints a message to a simple page.
        """

        return "Congratulations, it's a web app!"

    from . import db
    db.init_app(app)

    return app
