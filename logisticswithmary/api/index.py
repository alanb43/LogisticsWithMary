import flask
import logisticswithmary


@logisticswithmary.app.route('/api/v1/', methods=['GET'])
def get_index():
    """Return list of available services. Authentication not required."""
    context = {

    }
    
    return flask.jsonify(**context)
