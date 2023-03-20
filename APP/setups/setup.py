from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_gravatar import Gravatar

# Import the App
from .app_setup import AppSetup


# Create app
app_setup = AppSetup(website_name=('Green', 'Pole'))

app = app_setup.app

CKEditor(app)
Bootstrap(app)
CSRFProtect(app)
login_manager = LoginManager(app)

login_manager.login_view = "login"
login_manager.login_message = "Please log in to add, modify or delete a post. " \
                              "* Only administrators can do those operations. " \
                              "Contact the supervisor if you are not able to do so with an administrator account. *"
login_manager.login_message_category = "info"


db = SQLAlchemy(app)

Gravatar(app, size=100, rating='g', default='retro',
         force_default=False, force_lower=False, use_ssl=False, base_url=None)

app_setup.create_root()

render_page = app_setup.render_page
render_tool = app_setup.render_tool

secure_redirect = app_setup.secure_redirect

variables = app_setup.variables

WEBSITE_NAME = app_setup.variables['website_name']

# Create more pages here! ⬇

app_setup.add_template('login')
app_setup.add_template('register')
app_setup.add_template('profile')


# Ex.: app_setup.add_page('boutique')
# Then you need to munally add the page in the blueprint template folder.

# ----------------------- #
