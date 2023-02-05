#model.py database schema declaration and definition.from pymongo import MongoClient

from pymongo import MongoClient
from model.userAuth import user_auth_schema
from model.userDetails import user_details_schema

db_client = MongoClient('mongodb://localhost:27017/')
# db_client = MongoClient('mongodb+srv://emd:ems@cluster0.nqgydk1.mongodb.net/?retryWrites=true&w=majority')

class UserManagement:
    def __init__(self):
        self.clinet = db_client
        self.database = db_client["org_360"]
        database_names = db_client.list_database_names()
      
        if database_names.count("LMS") > 0:
            print("Database connected!")
        else:
            # self.database = db_client["LMS"]
            print("LMS database created")
        
    def create_collection(self, name, validation):
        self.database.create_collection(name, validator=validation)
    
    def check_collection(self, name):
        collection = self.database.list_collection_names()
        if collection.count(name) > 0:
            return True
        return False
        
    def user_auth(self):
        collection_exists = self.check_collection("user_auth")
        if collection_exists == False:
            self.create_collection("user_auth", user_auth_schema())
        return self.database["user_auth"]
    
    def user_details(self):
        collection_exists = self.check_collection("user_details")
        print(collection_exists)
        if collection_exists == False:
            try:
                self.create_collection("user_details", user_details_schema)
            except Exception as e:
                print(e)
        return self.database["user_details"]
    
            