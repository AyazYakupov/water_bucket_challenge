from config import settings
from openid import schema
from flasgger import Swagger
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


class AppContext:
    _app = None

    @classmethod
    def app(cls):
        if cls._app is None:
            cls._app = Flask(__name__)
            cls._app.secret_key = "!secret"

            # Initialze settings
            Swagger(cls._app, template=schema)

            cls._app.config.from_object("config.settings")
            if not settings.TESTING_ENV:
                # Rate limit to protect from brute-force attacks
                # and spambots.
                Limiter(
                    cls._app,
                    key_func=get_remote_address,
                    default_limits=["10 per second"],
                )
            # at this place we can put sentry logger/elk

        return cls._app


application = AppContext.app()
