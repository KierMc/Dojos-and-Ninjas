from flask import redirect, render_template, request
from flask_app import app
from flask_app.models import dojos_model
from flask_app.models import ninjas_model

@app.route('/')
def home():
    return redirect ('/dojos')

@app.route('/dojos')
def dojo_list():
    all_dojos = dojos_model.Dojo.get_all()
    return render_template ('index.html', dojos=all_dojos)

@app.route('/show/<int:id>')
def show_dojo_id(id):
    data={
        "id":id
    }
    return render_template('show.html', dojo=dojos_model.Dojo.get_ninjas_with_dojo(data))

@app.route('/create_dojo', methods=['POST'])
def new_dojo():
    dojos_model.Dojo.new_dojo(request.form)
    return redirect ('/dojos')


