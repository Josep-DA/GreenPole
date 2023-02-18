
# Import the App
from .app_setup import AppSetup

# Create app
app_setup = AppSetup(website_name=('Green', 'Pole'))

app = app_setup.app

render_page = app_setup.render_page
render_tool = app_setup.render_tool

secure_redirect = app_setup.secure_redirect

variables = app_setup.variables

WEBSITE_NAME = app_setup.variables['website_name']

# Create more pages here! ⬇

app_setup.add_template('mission')
app_setup.add_template('origin')
app_setup.add_template('founders')
app_setup.add_template('process')
app_setup.add_template('documentation')
app_setup.add_template('FAQ')


# Ex.: app_setup.add_page('boutique')
# Then you need to munally add the page in the blueprint template folder.

# ----------------------- #
