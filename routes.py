from flask import render_template, request

from models import Person

from app import db

def register_routes(app,db):
    @app.route('/')

    def index():
        print("DB path:", db.engine.url)
        people = Person.query.all()

        return str(people)