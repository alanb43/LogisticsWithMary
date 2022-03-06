from calendar import c
import flask
import logisticswithmary
from authenticator import Authentication
from error_handler import ErrorHandler

@logisticswithmary.app.route('/api/v1/orders/', methods=['GET'])
def get_orders() -> flask.Response:
    """
    Returns the latest 25 orders by default.
    Parameters allow for:
        latest x orders retrieval
        retreiving orders newer than x date
        retrieving orders older than x date
        retrieving orders between x and y dates
        pagination
    """

    Authentication()
    args = flask.request.args
    size = args.get('size', default=25, type=int)
    page = args.get('page', default=0, type=int)
    from_date = args.get('from', default='', type=str)
    to_date = args.get('to', default='', type=str)

    if size < 0 or page < 0 or is_bad_date(from_date, to_date):
        raise ErrorHandler(message="Bad Request", status_code=400)

    context = {

    }

    return flask.jsonify(**context)


def is_bad_date(from_date: str, to_date: str) -> bool:
    """Verifies legitimacy of user inputted dates in mm/dd/yyyy format."""
    from_split = from_date.split('/')
    to_split = to_date.split('/')
    if len(from_split) != 3 or len(to_split) != 3:
        return False
    
