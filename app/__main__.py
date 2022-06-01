from flask import Flask
from app import config


def create_app(scope: str = "dev"):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config.get_config(scope))
    from app.endpoints.generation.views import gen_view

    with flask_app.app_context():
        flask_app.register_blueprint(gen_view)

    return flask_app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
