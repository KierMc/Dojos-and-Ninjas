from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']

    @classmethod
    def get_ninjas_with_dojo(cls):
        query = "SELECT * FROM dojos JOIN ninjas ON dojo_id=%(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)

        return cls(results[0])

    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s)'
        new_ninja = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(new_ninja)
        return new_ninja