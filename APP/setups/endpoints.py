from flask import flash
from flask_login import login_user, login_required, logout_user, current_user
from .setup import app, render_page, variables, WEBSITE_NAME, secure_redirect, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from ..forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from ..crud_ops import *

# -------- Configuration -------- #

@login_manager.user_loader
def load_user(user_id):
    return get('User', user_id)

# -------- Pages' endpoints -------- #

# La page home est une page servant à diriger les utilisateurs vers les autres pages de la section recherches.
@app.route('/home')
def home():
    return render_page('home', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Home", current_li='app', disable_extra_part=(current_user.is_authenticated))

# #

# La page login est une page servant à connecter les utilisateurs au site.
@app.route('/login', methods=['Post', 'Get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)

        user = read('User', 'username', form.username.data)
        if user is not None:
            password = user.password
            print(check_password_hash(password, form.password.data), 'sdfusdygfuyjgfiuadst7fbiucylisabyfivbafniuesbh')
            if check_password_hash(password, form.password.data):
                login_user(user)
                pass
            else:
                flash('Le nom d\'utilisateur ou le mot de passe est incorrect.', 'danger')

                return secure_redirect('login', _bp_=False)
        else:
            flash('Le nom d\'utilisateur ou le mot de passe est incorrect.')
            return secure_redirect('login', _bp_=False)

        flash('Logged in successfully.')

        return secure_redirect('home', _bp_=False)

    return render_page('login', website_name=WEBSITE_NAME, form=form, add_navbar_footer=True, page_title="Login", current_li='app', disable_extra_part=None)

# #

# La page sign_in est une page servant à connecter les utilisateurs au site.
@app.route('/register', methods=['Post', 'Get'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        user = read('User', 'email', form.email.data)
        print(user)

        if user is None:
            user_firstname = form.firstname.data
            user_lastname = form.lastname.data
            user_email = form.email.data
            user_username = form.username.data
            user_password = generate_password_hash(
                password=form.password.data,
                method='pbkdf2:sha256',
                salt_length=25)

            user = create_user('User', user_firstname, user_lastname, user_username, user_email, user_password)
            form.reset_form()

            # login_user(user)
            flash('Registered successfully.')

            return secure_redirect('home', _bp_=False)
        else:
            flash('The email entered is already used.')
            del user
            return secure_redirect('register', _bp_=False)
        
    return render_page('register', website_name=WEBSITE_NAME, form=form, add_navbar_footer=True, page_title="Register", current_li='app', disable_extra_part=None)

# #

# La page profile est une page servant à observer ses informations personnelles.
@app.route('/profile', methods=['Post', 'Get'])
def profile():
     
    return render_page('profile', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Profile", current_li='app')

# #


# La page logout est une page servant à déconnecter les utilisateurs.
@app.route('/logout', methods=['Get'])
def logout():
    logout_user()
    return secure_redirect('home', _bp_=False)

# #

setup_done = "**//IMPORTANT//** -- All desktop endpoints have been setted! ECODE: DESK-001!"
