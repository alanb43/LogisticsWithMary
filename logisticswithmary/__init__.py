"""logisticswithmary package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (logisticswithmary/config.py)
app.config.from_object('logisticswithmary.config')

# Overlay settings read from a Python file whose path is set in the environment
# variable INSTA485_SETTINGS. Setting this environment variable is optional.
# Docs: http://flask.pocoo.org/docs/latest/config/
#
# EXAMPLE:
# $ export LOGISTICSWITHMARY_SETTINGS=secret_key_config.py
app.config.from_envvar('LOGISTICSWITHMARY_SETTINGS', silent=True)

# Tell JSON not to sort our keys for jsonify / dumps. Maintains order I set.
# stackoverflow.com/questions/
#   54446080/how-to-keep-order-of-sorted-dictionary-passed-to-jsonify-function
app.config['JSON_SORT_KEYS'] = False

# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
import logisticswithmary.api  # noqa: E402  pylint: disable=wrong-import-position
import logisticswithmary.views  # noqa: E402  pylint: disable=wrong-import-position
import logisticswithmary.model  # noqa: E402  pylint: disable=wrong-import-position
