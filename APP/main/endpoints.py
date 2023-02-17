from .setup import bp, render_page, variables, WEBSITE_NAME

# Pages' endpoints
@bp.route('/acceuil')
def acceuil():
    return render_page('acceuil', website_name=WEBSITE_NAME)

@bp.route('/recyclage')
def recyclage():
    return render_page('recyclage', website_name=WEBSITE_NAME)

@bp.route('/a-propos')
def a_propos():
    return render_page('a-propos', website_name=WEBSITE_NAME)

@bp.route('/blog')
def blog():
    return render_page('blog', website_name=WEBSITE_NAME)

@bp.route('/article-blog')
def article_blog():
    return render_page('article-blog', website_name=WEBSITE_NAME)

@bp.route('/contactez-nous')
def contactez_nous():
    return render_page('contactez-nous', website_name=WEBSITE_NAME)

# Database related

@bp.route('/connexion')
def connexion():
    return render_page('connexion', website_name=WEBSITE_NAME, current_page="connexion")

@bp.route('/enregistrement')
def enregistrement():
    return render_page('enregistrement', website_name=WEBSITE_NAME, current_page="enregistrement")

setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
