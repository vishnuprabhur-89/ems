#project database

def project_detail_schema():
    return {
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': [],
            'properties': {
                'project_id': {
                    'bsonType': 'string'
                },
                'project_name': {
                    'bsonType' : 'string'
                },
                'client': {
                    'bsonType' : 'string'
                },
                'strength': {
                    'bsonType': 'number'
                },
                'members': {
                    'bsonType': 'array'
                },
                
            }
        }
    }