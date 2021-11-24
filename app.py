from flask import Flask
from flask_restx import Api

from setup import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from config import Config

config = Config()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():



        with db.session.begin():
            db.session.add_all()


app = create_app()
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

