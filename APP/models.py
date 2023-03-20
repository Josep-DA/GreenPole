from .setups import db
from flask_login import UserMixin
import datetime


# CONFIGURE TABLES

# child = db.relationship('Child', backref='parent', uselist=False)
# parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    author = db.relationship('Author', backref='user', uselist=False)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<{self.__tablename__}: '{self.firstname}', '{self.lastname}', '{self.username}'," \
            f"'{self.email}', '{self.password}' >"
    

class Author(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    articles = db.relationship('Article', backref='author')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<{self.__tablename__}: '{self.firstname}', '{self.lastname}', '{self.username}'," \
            f"'{self.email}', '{self.sq}', '{self.sqanswer}', '{self.password}' >"


class Article(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    creationdate = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    image = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<{self.__tablename__}: '{self.firstname}', '{self.lastname}', '{self.username}'," \
            f"'{self.email}', '{self.sq}', '{self.sqanswer}', '{self.password}' >"

# class Comment(db.Model, UserMixin):
#     __tablename__ = "comments"

#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     author = relationship('User', back_populates="blog_comments")
#     blog_post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
#     blog_post = relationship('BlogPost', back_populates="blog_comments")

#     def to_dict(self):
#         return {column.name: getattr(self, column.name) for column in self.__table__.columns}

#     def __repr__(self):
#         return f"<{self.__tablename__}: '{self.text}', '{self.author_id}', '{self.date}' >"


# class BlogPost(db.Model):
#     __tablename__ = "blog_posts"

#     id = db.Column(db.Integer, primary_key=True)

#     author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

#     author = relationship("User", back_populates="posts")

#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=True)
#     date = db.Column(db.String(250), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)

#     blog_comments = relationship('Comment', back_populates="blog_post")

#     def to_dict(self):
#         return {column.name: getattr(self, column.name) for column in self.__table__.columns}

#     def __repr__(self):
#         return f"<{self.__tablename__}: '{self.author}', '{self.title}', '{self.subtitle}', '{self.date}', " \
#                f"'{self.body}', '{self.img_url}' >"



# class SocialPosts(db.Model, UserMixin):
#     __tablename__ = "socialposts"

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)

#     socialposts = relationship('BlogPost', back_populates="author")
#     blog_comments = relationship('Comment', back_populates="author")

#     def to_dict(self):
#         return {column.name: getattr(self, column.name) for column in self.__table__.columns}

#     def __repr__(self):
#         return f"<{self.__tablename__}:  '{self.email}', '{self.password}', '{self.name}', '{self.rank}' >"

# class Comment(db.Model, UserMixin):
#     __tablename__ = "comments"

#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     author = relationship('User', back_populates="blog_comments")
#     blog_post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
#     blog_post = relationship('BlogPost', back_populates="blog_comments")

#     def to_dict(self):
#         return {column.name: getattr(self, column.name) for column in self.__table__.columns}

#     def __repr__(self):
#         return f"<{self.__tablename__}: '{self.text}', '{self.author_id}', '{self.date}' >"

# db.create_all()



#
# create('BlogPost',
#        author='Angela Yu',
#        title='The Life of Cactus',
#        subtitle='Who knew that cacti lived such interesting lives.',
#        date='October 20, 2020',
#        body='<p>Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery.'
#             '</p><p>Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip.</p>'
#             '<p>Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut'
#             ' pea sierra leone bologi leek soko chicory celtuce parsley j&iacute;cama salsify.</p>',
#        img_url='https://images.unsplash.com/photo-1530482054429-cc491f61333b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1651&q=80'
#        )
