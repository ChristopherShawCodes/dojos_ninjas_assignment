from flask import render_template, request , redirect
from flask_app import app
#this allows us to talk to both model files 
from flask_app.models import ninja, dojo




#routes to ninjas page which is a form used to add a ninja to the dojo
@app.route('/ninjas')
def display_ninjas(): #from the model file named "dojo" call class of "Dojo" with a classmethod of get_all
    dojos = dojo.Dojo.get_all()
    #labeled dojos to be equal to all_dojos to clear method object not iterable error
    return render_template("ninjas.html", all_dojos = dojos)

#links with ninjas.html line 13, form action =/create/ninja
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    #model folder ninja, class  = "Ninja", save entry , note ninjas.html values match the column names on line 25,29 & 33
    ninja.Ninja.save(request.form)
    return redirect('/')








# @app.route('/user/edit/<int:id>')
# def edit_user(id):
#     data = {
#         "id":id
#     }
#     user=User.get_one(data)
#     return render_template('edit.html', user = user)



# @app.route('/user/update', methods=["POST"])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/user/destroy/<int:id>')
# def destroy(id):
#     data ={
#         'id': id
# }
#     User.destroy(data)
#     return redirect('/users')


# @app.route('/reset')
# def reset():
#     session.clear()
#     return redirect('/create')