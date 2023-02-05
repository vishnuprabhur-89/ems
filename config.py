from pymongo import MongoClient
import datetime

# MONGODB = MongoClient('mongodb://localhost:27017/')
MONGODB = MongoClient('mongodb+srv://emd:ems@cluster0.nqgydk1.mongodb.net/?retryWrites=true&w=majority')

DATABASE = "EMS"
SECRET_KEY = "LMS_LEVEL_ONE"
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
