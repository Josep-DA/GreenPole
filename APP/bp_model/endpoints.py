from .setup import bp, render_page, variables, WEBSITE_NAME

# Pages' endpoints
@bp.route('/acceuil')
def acceuil():
    return render_page('acceuil', website_name=WEBSITE_NAME)


# # Database related

# @bp.route('/connexion')
# def connexion():
#     return render_page('desktop', 'connexion', website_name=WEBSITE_NAME, current_page="connexion")

# @bp.route('/enregistrement')
# def enregistrement():
#     return render_page('desktop', 'enregistrement', website_name=WEBSITE_NAME, current_page="enregistrement")

setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
