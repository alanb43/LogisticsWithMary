"""Handles all API authentication."""
import flask
import logisticswithmary
from logisticswithmary.api.error_handler import ErrorHandler
# from logisticswithmary.views.accounts import encrypt


# UPDATE TO ONLY ALLOW SESSION, NOT HTTP
class Authentication():
    """Authentication for API only using session auth."""

    def __init__(self):
        """Initialize class. Call get_auth()."""
        # No need for auth when testing basic api functionality
        return
        
        self.username = None
        self.password = None

        if "logged_user" not in flask.session.keys():
            self.get_auth()
            if self.verify_auth():
                flask.session["logged_user"] = self.username
            else:
                raise ErrorHandler(message="Forbidden",
                                    status_code=403)

    def get_auth(self):
        """User can use sessions and authenication."""
        if "username" in flask.request.form.keys():
            self.username = flask.request.form['username']
            self.password = flask.request.form['password']
            print("json/form")
        elif flask.request.authorization is not None:
            self.username = flask.request.authorization['username']
            self.password = flask.request.authorization['password']
            print("authorization")

    def verify_auth(self):
        """Check if a user exists in the database."""
        if self.username is None or self.password is None:
            return False

        connection = logisticswithmary.model.get_db()
        user_info = connection.execute("""
            SELECT password FROM users
             WHERE username = ?
        """, (self.username,)).fetchall()

        if len(user_info) == 0:
            return False

        _password = user_info[0]['password']
        _salt = _password[7: _password.rfind('$')]
        # encrypted_pass = encrypt(self.password, _salt)
        encrypted_pass = "FIXME"
        return encrypted_pass == _password

    def get_username(self):
        """Return username."""
        self.username = flask.session["logged_user"]
        return self.username
