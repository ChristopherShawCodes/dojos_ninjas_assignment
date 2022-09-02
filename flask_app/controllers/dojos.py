from flask import render_template, redirect, request
from flask_app import app
#import the class of Dojo from models folder --> dojo.py
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

#routes to dojos or the home page for this assignment
@app.route('/dojos')
def dojos():
    #get_all refers to the class method of get_all found in models --> dojo
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

#Routes to /create/dojo referenced in index.html form action="/create/dojo" line 14
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #references the class of Dojo from Models -->dojo.py(singular) and the classmethod of "save"
    Dojo.save(request.form) #request.form is a dictionary and coorelates to index.html line 18 name=name
    return redirect('/dojos')

#route from  index.html a href="/dojo/{{a_dojo.id}}"
@app.route('/dojo/<int:id>')
def show_ninjas_from_a_dojo(id):
    data={
        "id": id
    }
    return render_template('show.html' , dojo=Dojo.display_ninjas_from_a_dojo(data))
