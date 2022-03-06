import flask
import logisticswithmary
from logisticswithmary.api.authenticator import Authentication
from logisticswithmary.api.error_handler import ErrorHandler

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

    # Authentication()
    args = flask.request.args
    # either size / page params used or dates used to query db
    # default behavior with no params: grab 10 latest orders
    # default behavior with dates: grab all in time range
    size = 10
    page = args.get('page', default=0, type=int)
    from_date = args.get('from', default='', type=str)
    to_date = args.get('to', default='', type=str)

    if page < 0 or is_bad_date(from_date) or is_bad_date(to_date):
        raise ErrorHandler(message="Bad Request", status_code=400)

    context = get_unfulfilled(size, page, from_date, to_date)

    return flask.jsonify(**context)


def get_unfulfilled(size, page, from_date, to_date):
    """Return unfulfilled orders based on parameters from request querys."""
    unfulfilled = []
    if from_date != '' or to_date != '':
        data = get_unfulfilled_between_dates_from_db(page, from_date, to_date)
    else:
        data = get_unfulfilled_from_db(size, page)

    for order in data:
        orderid = order['orderid']
        order_dict = {
            "orderid": orderid,
            "url": f"/api/v1/orders/{orderid}/"
        }
        
        unfulfilled.append(order_dict)
        if len(unfulfilled) >= size:
            break

    if len(data) == size:
        next_url = "/api/v1/orders/"
        next_url += f"?page={page + 1}"
    else:
        next_url = ""

    return {
        "next": next_url,
        "unfulfilled": unfulfilled
    }

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
    print(data)
    return data


def get_unfulfilled_between_dates_from_db(size, page, from_date, to_date):
    """Query database for unfulfileld orders based on paramters."""
    connection = logisticswithmary.model.get_db()

    # Supposed to query between a range of dates
    if from_date == '' and to_date == '':
        error_msg = "ERROR: date range query used when dates aren't provided."
        print(error_msg)
        return error_msg
    # if from isn't provided, select everything up until and including to_date
    elif from_date == '':
        from_date = '00000000'
    # if to isn't provided, select everything from and after from_date
    elif to_date == '':
        to_date = '99999999'

    cur = connection.execute("""
        SELECT orderid, name, clothingarticle, size, color, design, orderedorstocked,
            pricecharged, shipped, shippingaddress, completeby, notes, created 
        FROM unfulfilled 
        WHERE created >= ? and created <= ? 
        LIMIT ?,?;
    """, (from_date, to_date, page * size, size))

    data = cur.fetchall()

    return data


def is_bad_date(date: str) -> bool:
    """Verify legitimacy of user inputted date in mm/dd/yyyy format."""
    if date == '':
        return False

    date_split = date.split('/')
    if len(date_split) != 3:
        return True

    mm, dd, yyyy = date[0:3]
    
    if not mm.isdigit() or not dd.isdigit() or not yyyy.isdigit():
        return True
    if mm < 1 or dd < 1 or yyyy < 2022:
        return True
    if mm > 12 or dd > 31:
        return True

    return False


def count_num_posts(orderid):
    """Count the number of posts older than <orderid>."""
    connection = logisticswithmary.model.get_db()
    cur = connection.execute("""
        SELECT COUNT(*)
         FROM unfulfilled
          WHERE orderid <= ?
    """, (orderid,))
    num_posts = cur.fetchall()[0]["COUNT(*)"]

    return num_posts
