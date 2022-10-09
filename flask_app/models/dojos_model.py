from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models.ninjas_model import Ninja

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.ninjas=[]
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos=[]

        for dojo in results:
            instance=cls(dojo)
            dojos.append(instance)

        return dojos

    @classmethod
    def get_ninjas_with_dojo(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojo_id=dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if (results):
            dojo=cls(results[0])

            for row_from_db in results:
                ninja_data={
                    "id": row_from_db["ninjas.id"],
                    "first_name": row_from_db["first_name"],
                    "last_name": row_from_db["last_name"],
                    "age": row_from_db["age"],
                    "created_at": row_from_db["created_at"],
                    "updated_at": row_from_db["updated_at"]
                }

                dojo.ninjas.append(Ninja(ninja_data))
            
            return dojo

    @classmethod
    def new_dojo(cls, data):
        print(data)
        query = 'INSERT INTO dojos (name, created_at) '
        query += 'VALUES(%(name)s, NOW())'
        new_dojo = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return new_dojo