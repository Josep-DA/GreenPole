
# Import the Blueprint
from .blueprint_setup import BluprintSetup

blueprint_setup = BluprintSetup(
    name='blog', website_name=('Green', 'Pole'))

bp = blueprint_setup.bp

render_page = blueprint_setup.render_page
render_tool = blueprint_setup.render_tool

secure_redirect = blueprint_setup.secure_redirect

variables = blueprint_setup.variables

WEBSITE_NAME = blueprint_setup.variables['website_name']

# Create more pages here! ⬇

blueprint_setup.add_template('article')



# Ex.: blueprint_setup.add_page('boutique')
# Then you need to munally add the page in the blueprint template folder.

# ----------------------- #
