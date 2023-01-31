
# Import the Blueprint
from .blueprint_setup import BluprintSetup

blueprint_setup = BluprintSetup(name='desktop', language='french')
blueprint_setup.set_website_name('QG-Info')

bp = blueprint_setup.bp

render_page = blueprint_setup.render_page
render_tool = blueprint_setup.render_tool

secure_redirect = blueprint_setup.secure_redirect

variables = blueprint_setup.variables

WEBSITE_NAME = blueprint_setup.variables['website_name']

# Create more pages here! ⬇


# Ex.: blueprint_setup.add_page('boutique')
# Then you need to munally add the page in the blueprint template folder.

# ----------------------- #
