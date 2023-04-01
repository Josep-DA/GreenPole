from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL, Email
from wtforms.fields.html5 import EmailField  
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title:", validators=[DataRequired()])
    author = StringField("Author:", validators=[DataRequired()])
    img_url = StringField("Blog Image URL:", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content:", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

    def reset_form(self):
        self.title.data = ''
        self.author.data = ''
        self.img_url.data = ''
        self.body.data = ''


class RegisterForm(FlaskForm):
    firstname = StringField(validators=[DataRequired()], 
                           render_kw={"class_":"data-entry", "placeholder":"First Name"})
    lastname = StringField(validators=[DataRequired()], 
                           render_kw={"class_":"data-entry", "placeholder":"Last Name"})

    email = EmailField(validators=[DataRequired(), Email()],
                        render_kw={"class":"data-entry", "placeholder": "Email"})
    
    username = StringField(validators=[DataRequired()], 
                           render_kw={"class_":"data-entry", "placeholder":"Username"})
    
    password = PasswordField( validators=[DataRequired()], 
                             render_kw={"class_":"data-entry", "placeholder":"Password"})
    
    password2 = PasswordField(validators=[DataRequired()], 
                             render_kw={"class_":"data-entry", "placeholder":"Enter Password Again"})
    
    submit = SubmitField(render_kw={"id":"submit-btn"})

    def reset_form(self):
        self.firstname = ''
        self.lastname = ''
        self.email = ''
        self.username = ''
        self.password = ''
        self.password2 = ''
        self.submit = ''


class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()], 
                           render_kw={"class_":"data-entry", "placeholder":"Username"})
    password = PasswordField("Password:", validators=[DataRequired()], 
                             render_kw={"class_":"data-entry", "placeholder":"Password"})

    submit = SubmitField("Connexion",
                         render_kw={"id":"submit-btn"})

    def reset_form(self):
        self.email.data = ''
        self.password.data = ''


class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()], render_kw={"placeholder": "Leave a comment!"})
    submit = SubmitField("Submit Comment")

    def reset_form(self):
        self.body.data = ''
