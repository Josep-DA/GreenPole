from flask import url_for
from .setup import app, render_page, variables, WEBSITE_NAME, secure_redirect

# -------- Pages' endpoints -------- #

# La page home est une page servant à diriger les utilisateurs vers les autres pages de la section recherches.
@app.route('/home')
def home():
    return render_page('home', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Home", current_li='app')

# #


# L'url /recherche sert à rediriger vers la section recherches.'
@app.route('/recherches')
def recherches():
    return secure_redirect('recherches.root')

# #


setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
