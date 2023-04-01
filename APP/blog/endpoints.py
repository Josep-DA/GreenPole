from .setup import bp, render_page, variables, WEBSITE_NAME, secure_redirect
from flask_login import login_user, login_required, logout_user, current_user
from flask import flash
from ..crud_ops import *
from ..forms import *
from ..models import *


# -------- Pages' endpoints -------- #
is_published = None
messaged:int = 0
def published(state):
    global messaged
    global is_published

    if state is not None:
        is_published = state

    if state is None:
        if messaged == 1:
            is_published = None
            messaged = 0
        else:
            messaged +=1
        return is_published


# La page home est une page servant à diriger les utilisateurs vers les autres pages de la section recherches.
def get_all_articles():
    all_articles = read_all('Article')
    return all_articles

@bp.route('/home')
def home():
    return render_page(
        'home', all_articles=get_all_articles(),
        website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Home", 
        current_li=bp.name, disable_extra_part=(current_user.is_authenticated)
        )

# #


# La page mission est une page parlant de notre objectif et de celui du mouvement GreenPole.
@bp.route('/article/<article_id>')
def article(article_id):
    return render_page('article', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Article", current_li=bp.name, disable_extra_part=(current_user.is_authenticated))

# #

# La page mission est une page parlant de notre objectif et de celui du mouvement GreenPole.
@bp.route('/example_article')
def example_article():
    return render_page('example_article', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Example_article", current_li=bp.name, disable_extra_part=(current_user.is_authenticated))

# #

# La page mission est une page parlant de notre objectif et de celui du mouvement GreenPole.
@bp.route('/editing',  methods=['Post', 'Get'])
def editing():
    form = CreatePostForm()
    if form.validate_on_submit():
        published(False)
        new_article = Article(
            title=form.title.data,
            content=form.body.data,
            image=form.img_url.data,
            author_name=form.author.data
        )
        db.session.add(new_article)
        db.session.commit()
        published(True)
        return secure_redirect("editing")
    return render_page('editing', form=form, is_published=published(None), website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Editing", current_li=bp.name, disable_extra_part=(current_user.is_authenticated))

# #


setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
