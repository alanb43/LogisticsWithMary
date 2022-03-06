import flask
import logisticswithmary


@logisticswithmary.app.route('/', methods=['GET'])
def show_index():
    """Render index page for contact get request."""
    return flask.render_template("index.html")
