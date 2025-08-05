from flask import render_template, request

from models import Person

from app import db

def register_routes(app,db):
    @app.route('/', methods = ['POST', 'GET'])

    def index():
        if request.method == "GET":
            print("DB path:", db.engine.url)
            people = Person.query.all()

            return render_template('index.html', people = people)
        
        elif request.method == "POST":
            name = request.form.get('name')
            age = int(request.form.get('age'))

            person = Person(name=name, age=age,)

            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template('index.html', people = people)
        

        





