from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
# from flask_login import LoginManager
from flask_gravatar import Gravatar
from .setups.app_setup import AppSetup

app_setup = AppSetup(website_name=('Green', 'Pole'))
app = app_setup.app

from .setups.config import Config

app.config.from_object(Config)


CKEditor(app)
CSRFProtect(app)
# login_manager = LoginManager(app)

# login_manager.login_view = "login"
# login_manager.login_message = "Please log in to add, modify or delete a post. " \
#                               "* Only administrators can do those operations. " \
#                               "Contact the supervisor if you are not able to do so with an administrator account. *"
# login_manager.login_message_category = "info"


db = SQLAlchemy(app)

Gravatar(app, size=100, rating='g', default='retro',
         force_default=False, force_lower=False, use_ssl=False, base_url=None)

this_app_setup = app_setup
