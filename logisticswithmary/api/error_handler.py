"""
Error response class for LogisticsWithMary API.

Original writing from flask documentation: 
    https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/

Adapted by Alan Bergsneider <bera@umich.edu> (myself)
for insta485 for EECS 485 at the University of Michigan,
and now this.
"""
import flask
import logisticswithmary


class ErrorHandler(Exception):
    """Error response class for API."""

    def __init__(self, *args: object, message: str, status_code: int) -> None:
        """Init."""
        super().__init__(*args)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        """Jsonify error."""
        err = {
            "message": self.message,
            "status_code": self.status_code,
        }

        return err


@logisticswithmary.app.errorhandler(ErrorHandler)
def handle_invalid_usage(error):
    """Flask handle invalid usage function (from docs)."""
    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
