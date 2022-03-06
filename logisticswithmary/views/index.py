import flask
import logisticswithmary


@logisticswithmary.app.route('/', methods=['GET'])
def get_contact():
    """Render index page for contact get request."""
    return flask.render_template("index.html")
