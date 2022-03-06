"""
API unfulfilled order routes serviced here.

Routes:
/api/v1/orders/
/api/v1/order/<orderid>/
"""
import flask
import logisticswithmary
from logisticswithmary.api.authenticator import Authentication
from logisticswithmary.api.error_handler import ErrorHandler


@logisticswithmary.app.route('/api/v1/orders/', methods=['GET'])
def get_orders() -> flask.Response:
    """
    Returns the latest 10 orders by default.
    Query parameters allow for:
        pagination
        retreiving orders newer than x date
        retrieving orders older than x date
        retrieving orders between x and y dates
    """

    Authentication()
    args = flask.request.args
    size = 10
    page = args.get('page', default=0, type=int)
    from_date = args.get('from', default=0, type=int)
    to_date = args.get('to', default=99999999, type=int)

    if page < 0 or is_bad_date(from_date) or is_bad_date(to_date):
        raise ErrorHandler(message="Bad Request", status_code=400)

    context = get_unfulfilled(size, page, from_date, to_date)

    return flask.jsonify(**context)


@logisticswithmary.app.route('/api/v1/order/<orderid>/', methods=['GET'])
def get_order(orderid) -> flask.Response:
    """Return json context for a given orderid."""

    Authentication()
    data = get_single_unfulfilled_from_db(orderid)
    if len(data) == 0:
        raise ErrorHandler(message="Not Found", status_code=404)

    context = {
        "name": data["name"],
        "clothingarticle": data["clothingarticle"],
        "size": data["size"],
        "color": data["color"],
        "design": data["design"],
        "orderedorstocked": data["orderedorstocked"],
        "pricecharged": data["pricecharged"],
        "shipped": data["color"],
        "shippingaddress": data["shippingaddress"],
        "completeby": data["completeby"],
        "notes": data["notes"],
        "created": data["created"],
    }

    return flask.jsonify(**context)


def get_unfulfilled(size, page, from_date, to_date):
    """Return unfulfilled orders based on parameters from request querys."""
    unfulfilled = []
    if from_date != '' or to_date != '':
        data = get_unfulfilled_between_dates_from_db(size, page, from_date, to_date)
    else:
        data = get_unfulfilled_from_db(size, page)

    for order in data:
        orderid = order['orderid']
        order_dict = {
            "orderid": orderid,
            "url": f"/api/v1/orders/{orderid}/"
        }
        
        unfulfilled.append(order_dict)

    if len(data) == size:
        next_url = f"/api/v1/orders/?page={page + 1}"
    else:
        next_url = ""

    context = {
        "next": next_url,
        "unfulfilled": unfulfilled
    }

    return context


def get_single_unfulfilled_from_db(orderid):
    """Query database for singular unfulfilled order."""
    connection = logisticswithmary.model.get_db()

    cur = connection.execute("""
        SELECT name, clothingarticle, size, color, design, orderedorstocked,
            pricecharged, shipped, shippingaddress, completeby, notes, created 
        FROM unfulfilled 
        WHERE orderid = ?
    """, (orderid, ))

    data = cur.fetchone()

    return data

def get_unfulfilled_from_db(size, page_offset):
    """Query database for unfulfileld orders based on paramters."""
    connection = logisticswithmary.model.get_db()
    # Uses LIMIT offset, row_count; syntax
    # ie : LIMIT 10, 5; returns 5 rows starting from 11th row
    cur = connection.execute("""
        SELECT orderid, name, clothingarticle, size, color, design, orderedorstocked,
            pricecharged, shipped, shippingaddress, completeby, notes, created 
        FROM unfulfilled 
        ORDER BY orderid DESC 
        LIMIT ?, ?;

    """, (page_offset * size, size))

    data = cur.fetchall()

    return data


def get_unfulfilled_between_dates_from_db(size, page_offset, from_date, to_date):
    """Query database for unfulfileld orders based on paramters."""
    connection = logisticswithmary.model.get_db()
    # Supposed to query between a range of dates
    if from_date == '' and to_date == '':
        error_msg = "ERROR: date range query used when dates aren't provided."
        print(error_msg)
        return error_msg


    cur = connection.execute("""
        SELECT orderid, name, clothingarticle, size, color, design, orderedorstocked,
            pricecharged, shipped, shippingaddress, completeby, notes, created 
        FROM unfulfilled 
        WHERE created >= ? and created <= ? 
        ORDER BY orderid DESC 
        LIMIT ?,?;
    """, (from_date, to_date, page_offset * size, size))
    print(from_date, to_date)
    data = cur.fetchall()

    return data


def is_bad_date(date: int) -> bool:
    """Verify legitimacy of user inputted date in mm/dd/yyyy format."""
    if date == 0 or date == 99999999:
        return False
    
    date_str = str(date)
    mm, dd, yyyy = int(date_str[4:6]), int(date_str[6:8]), int(date_str[0:4])
    if mm < 1 or dd < 1 or yyyy < 2021:
        return True
    if mm > 12 or dd > 31:
        return True

    return False


def count_num_posts(orderid):
    """Count the number of orders older than <orderid>."""
    connection = logisticswithmary.model.get_db()
    cur = connection.execute("""
        SELECT COUNT(*)
         FROM unfulfilled
          WHERE orderid <= ?
    """, (orderid,))
    num_posts = cur.fetchall()[0]["COUNT(*)"]

    return num_posts
