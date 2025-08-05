from flask import render_template, request, url_for, redirect

from models import Person

from app import db

def register_routes(app,db):
    @app.route('/', methods = ['POST', 'GET'])
    def index():
        if request.method == "GET":
            print("DB path:", db.engine.url)
            people = Person.query.all()
            return render_template('index.html', people=people)
        
        elif request.method == "POST":
            name = request.form.get('name')
            age = int(request.form.get('age'))

            person = Person(name=name, age=age)
            db.session.add(person)
            db.session.commit()

            # Redirecting to GET after POST to prevent duplicate on reload
            return redirect(url_for('index'))
        
    # @app.route('/clear_all')

    # def clear_all():
    #     db.session.query(Person).delete()
    #     db.session.commit()
    #     return render_template('index.html')
    

    @app.route('/delete/<int:pid>', methods=['POST'])
    def delete_pid(pid):
        print(f"Deleting person with pid={pid}")
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        return redirect(url_for('index'))

    
    @app.route('/detail/<int:pid>')
    def detail(pid):
        person = Person.query.filter(Person.pid==pid).first()

        return render_template('detail.html',person=person)
    

    @app.route('/update_things/<int:pid>', methods = ['GET', 'POST'])
    def update_things(pid):
        person = Person.query.get(pid)
        if request.method == 'POST':
            person.name = request.form.get('name')
            person.age = request.form.get('age')

            db.session.commit()

            return redirect(url_for('index'))


        return render_template('update_things.html', person=person)        

        

        





