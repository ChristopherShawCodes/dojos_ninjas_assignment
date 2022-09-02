from flask_app.config.mysqlconnection import connectToMySQL
#use dot notation to call on a file within the same folder
from .ninja import Ninja


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#class method to display all dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        dojos = []
        print(dojos)
        for a_dojo in results:  
            dojos.append(cls(a_dojo))
        return dojos

    #class method to create a new dojo , returns the ID of the ROW !
    @classmethod
    def save(cls,data):
        #Here we are inserting a new entry into the dojos table where name will equal name
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        #Result to be the data we entered
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def display_ninjas_from_a_dojo(cls,data):
        # Select all from dojos and join them together via their ids and filter by user selected Dojo
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
        dojo.ninjas.append(Ninja(n))
        return dojo