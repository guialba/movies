from portal import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

watched_movies = db.Table('Watched_movies', Base.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('date', db.DateTime),
    db.Column('score', db.Float)
)
movie_roles = db.Table('Movie_roles', Base.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)
movie_countries = db.Table('Movie_countries', Base.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('country_id', db.Integer, db.ForeignKey('country.id'))
)
movie_languages = db.Table('Movie_languages', Base.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('language_id', db.Integer, db.ForeignKey('language.id'))
)
movie_genres = db.Table('Movie_genres', Base.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    watched = db.relationship("Movie", secondary=watched_movies)

    def __repr__(self):
        return '<User {}>'.format(self.username)    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True)
    original_title = db.Column(db.String(20), index=True)
    year = db.Column(db.Integer)
    original_air_date = db.Column(db.DateTime)
    runtimes = db.Column(db.Integer)
    rating = db.Column(db.Float)
    top_250_rank =db.Column(db.Numeric)
    budget = db.Column(db.Float)
    worldwide_gross = db.Column(db.Float)
    opening_weekend_US_gross = db.Column(db.Float)
    opening_weekend_US_date = db.Column(db.DateTime)
    people = db.relationship("Person", secondary=movie_roles, back_populates="movies")
    roles = db.relationship("Role", secondary=movie_roles)
    countries = db.relationship("Country", secondary=movie_countries, back_populates="movies")
    languages = db.relationship("Language", secondary=movie_languages, back_populates="movies")
    genres = db.relationship("Genre", secondary=movie_genres, back_populates="movies")


    def __repr__(self):
        return '<Movie {}>'.format(self.title)    

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    movies = db.relationship("Movie", secondary=movie_roles, back_populates="people")
    roles = db.relationship("Role", secondary=movie_roles, back_populates="people")

    def __repr__(self):
        return '<Person {}>'.format(self.name) 

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), index=True)
    people = db.relationship("Person", secondary=movie_roles, back_populates="roles")

    def __repr__(self):
        return '<Role {}>'.format(self.role) 

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), index=True)
    movies = db.relationship("Movie", secondary=movie_countries, back_populates="countries")

    def __repr__(self):
        return '<Country {}>'.format(self.country) 

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(50), index=True)
    movies = db.relationship("Movie", secondary=movie_languages, back_populates="languages")

    def __repr__(self):
        return '<Language {}>'.format(self.language) 

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), index=True)
    movies = db.relationship("Movie", secondary=movie_genres, back_populates="genres")

    def __repr__(self):
        return '<Genre {}>'.format(self.genre) 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))