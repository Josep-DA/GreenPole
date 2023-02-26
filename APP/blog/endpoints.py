from .setup import bp, render_page, variables, WEBSITE_NAME

# -------- Pages' endpoints -------- #

# La page home est une page servant à diriger les utilisateurs vers les autres pages de la section recherches.


@bp.route('/home')
def home():
    return render_page('home', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Home", current_li=bp.name)

# #


# La page mission est une page parlant de notre objectif et de celui du mouvement GreenPole.
@bp.route('/article/<article_id>')
def article(article_id):
    return render_page('article', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Article", current_li=bp.name)

# #


setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
