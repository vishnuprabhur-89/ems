from pymongo import MongoClient  # middleware between flask and mongodb
from config import MONGODB, DATABASE

class EMSinfo:
    def __init__(self):    
        self.clinet =  MONGODB
        self.database = self.clinet[DATABASE]
        
    def userInfo(self):
        collection = self.database.userInfo
        return collection
    
    def userProfile(self):
        collection = self.database.userProfile
        return collection