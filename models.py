from config import MONGODB, DATABASE

class EMSinfo:
    def __init__(self):
        self.clinet = MONGODB
        self.database = self.clinet[DATABASE]
       
    # def create_collection(self):
        # self.database.create_collection('schema_sample', validator={
            # '$jsonSchema': {
                # 'bsonType': 'object',
                # 'additionalProperties': True,
                # 'required': ['component', 'path'],
                # 'properties': {collection.find_one({'username' : current_user})
                    # 'component': {
                        # 'bsonType': 'string',
                    # },
                    # 'path': {
                        # 'bsonType': 'string',
                        # 'description': 'Set to default value'
                    # },
                    # '_id': {
                         # 'bsonType': 'string',
                    # }
                # }
            # }
        # })

    def userInfo(self):
        collection = self.database.userInfo
        return collection

    def userProfile(self):
        collection = self.database.userProfile
        return collection

    def schema(self):
        collection = self.database.schema_sample
        return collection
