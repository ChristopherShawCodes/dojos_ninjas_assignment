from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.dojo_id = data['dojo_id']



    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)









#     @classmethod
#     def update(cls,data):
#         query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
#         return connectToMySQL('users_schema').query_db(query,data)

#     @classmethod
#     def destroy(cls,data):
#         query  = "DELETE FROM users WHERE id = %(id)s;"
#         return connectToMySQL('users_schema').query_db(query,data)