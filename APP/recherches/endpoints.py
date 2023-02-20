from .setup import bp, render_page, variables, WEBSITE_NAME

# -------- Pages' endpoints -------- #

# La page home est une page servant à diriger les utilisateurs vers les autres pages de la section recherches.


@bp.route('/home')
def home():
    return render_page('home', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Home", current_li=bp.name, disable_extra_part=False)

# #


# La page mission est une page parlant de notre objectif et de celui du mouvement GreenPole.
@bp.route('/mission')
def mission():
    return render_page('mission', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Mission", current_li=bp.name, disable_extra_part=False)

# #


# La page origin est une page parlant de l'origine du projet GreenPole et de pourquoi il a été réalisé.
@bp.route('/origin')
def origin():
    return render_page('origin', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Origin", current_li=bp.name, disable_extra_part=False)

# #


# La page founders est une page parlant des créateurs à l'origine de ce projet et de pourquoi il ont participé à la création de ce projet.
@bp.route('/founders')
def founders():
    return render_page('founders', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Founders", current_li=bp.name, disable_extra_part=False)

# #


# La page process est une page parlant des étapes de réalisation du projet GreenPole.
@bp.route('/process')
def process():
    return render_page('process', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Process", current_li=bp.name, disable_extra_part=False)

# #


# La page documentation est une page donnat accès à une partie de la documentation du projet GreenPole.
@bp.route('/documentation')
def documentation():
    return render_page('documentation', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Documentation", current_li=bp.name, disable_extra_part=False)

# #


# La page FAQ est une page où les utilisateurs peuvent poser des questions sur le projet GreenPole.
@bp.route('/FAQ')
def faq():
    return render_page('FAQ', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="FAQ", current_li=bp.name, disable_extra_part=False)

# #


setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
