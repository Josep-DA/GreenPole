from flask import url_for
from .setup import app, render_page, variables, WEBSITE_NAME, secure_redirect

# -------- Pages' endpoints -------- #

# La page home est une page servant à diriger les utilisateurs vers les autres pages de la section recherches.
@app.route('/home')
def home():
    return render_page('home', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Home", current_li='app', disable_extra_part=False)

# #

# La page login est une page servant à connecter les utilisateurs au site.
@app.route('/login')
def login():
    return render_page('login', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Login", current_li='app')

# #

# La page sign_in est une page servant à connecter les utilisateurs au site.
@app.route('/register')
def register():
    return render_page('register', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Register", current_li='app')

# #

setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
