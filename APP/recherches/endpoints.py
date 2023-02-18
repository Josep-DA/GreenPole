from .setup import bp, render_page, variables, WEBSITE_NAME

# -------- Pages' endpoints -------- #

# La page d'accueil est une page servant à diriger les utilisateurs vers les autres pages de la section recherches.
@bp.route('/acceuil')
def acceuil():
    return render_page('acceuil', website_name=WEBSITE_NAME)

# #


# La page mission est une page parlant de notre objectif et de celui du mouvement GreenPole.
@bp.route('/mission')
def mission():
    return render_page('mission', website_name=WEBSITE_NAME)

# #


# La page origine est une page parlant de l'origine du projet GreenPole et de pourquoi il a été réalisé.
@bp.route('/origine')
def origine():
    return render_page('origine', website_name=WEBSITE_NAME)

# #


# La page fondateurs est une page parlant des créateurs à l'origine de ce projet et de pourquoi il ont participé à la création de ce projet.
@bp.route('/fondateurs')
def fondateurs():
    return render_page('fondateurs', website_name=WEBSITE_NAME)

# #


# La page parcours est une page parlant des étapes de réalisation du projet GreenPole.
@bp.route('/parcours')
def parcours():
    return render_page('parcours', website_name=WEBSITE_NAME)

# #


# La page documentation est une page donnat accès à une partie de la documentation du projet GreenPole.
@bp.route('/documentation')
def documentation():
    return render_page('documentation', website_name=WEBSITE_NAME)

# #


# La page foires-aux-questions est une page où les utilisateurs peuvent poser des questions sur le projet GreenPole.
@bp.route('/foires-aux-questions')
def foires_aux_questions():
    return render_page('foires-aux-questions', website_name=WEBSITE_NAME)

# #

setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
