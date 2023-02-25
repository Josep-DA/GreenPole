from flask import url_for
from .setups import app_setup
from .setups.server_setup import ServerSetup
from .main import bp as main_bp
from .recherches import bp as recherches_bp
from .blog import bp as blog_bp
from .social import bp as social_bp


# Blueprints
app_setup.register_blueprint(main_bp)
app_setup.register_blueprint(recherches_bp)
app_setup.register_blueprint(blog_bp)
app_setup.register_blueprint(social_bp)


# Create server & Link app to server
app = app_setup.app
server_setup = ServerSetup(_app_=app)


# Run server
def start_app(deployment: str = ''):
    if deployment != '':
        server_setup.run_app(deploy_option=deployment)
    else:
        print('ok')
        server_setup.run_app()