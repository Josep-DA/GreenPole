from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/greenpole.db"
db = SQLAlchemy(app)

from flask_login import UserMixin
from sqlalchemy.orm import relationship

# CONFIGURE TABLES


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    rank = db.Column(db.String(250), nullable=False)

    posts = relationship('BlogPost', back_populates="author")
    blog_comments = relationship('Comment', back_populates="author")

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<{self.__tablename__}:  '{self.email}', '{self.password}', '{self.name}', '{self.rank}' >"


class Comment(db.Model, UserMixin):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship('User', back_populates="blog_comments")
    blog_post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    blog_post = relationship('BlogPost', back_populates="blog_comments")

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<{self.__tablename__}: '{self.text}', '{self.author_id}', '{self.date}' >"


class Blog(db.Model):
    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")

    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    blog_comments = relationship('Comment', back_populates="blog_post")

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<{self.__tablename__}: '{self.author}', '{self.title}', '{self.subtitle}', '{self.date}', " \
               f"'{self.body}', '{self.img_url}' >"


db.create_all()
