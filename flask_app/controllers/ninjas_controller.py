from flask import redirect, render_template, request
from flask_app import app
from flask_app.models import dojos_model, ninjas_model

@app.route('/ninjas')
def new_ninja():
    return render_template('new.html', dojos=dojos_model.Dojo.get_all())

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    ninjas_model.Ninja.create_ninja(request.form)
    return redirect ('/dojos')