from flask import Flask

from app import config
from app.endpoints.auth import login_view
from app.endpoints.generation import gen_view
from app.endpoints.generators import generators_view
from app.endpoints.vault import vault_view
from app.modules import db, jwt, cors


def create_app(scope: str = "dev"):
    """Econokey Backend App Factory"""
    econokey = Flask(__name__)
    econokey.config.from_object(config.get_config(scope))
    econokey.url_map.strict_slashes = False
    view_list = [gen_view, generators_view, vault_view, login_view]
    with econokey.app_context():
        cors.init_app(econokey)
        # Register available endpoint blueprints
        for view in view_list:
            econokey.register_blueprint(view)

        # Initialize SQLAlchemy ORM
        db.init_app(econokey)
        db.create_all(app=econokey)
        db.session.commit()

        # Initialize JWT manager
        jwt.init_app(econokey)

    return econokey


econokey = create_app()
