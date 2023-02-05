#user register and login credentials schema

def user_auth_schema():
    return {
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['username', 'password', 'role'],
            'properties': {
                    'username': {
                        'bsonType': 'string'
                    },
                    'password': {
                        'bsonType': 'string',
                        'description': 'Set to default value'
                    },
                    'role': {
                        'bsonType': 'string',
                        'enum': ['ADMIN', 'EMPLOYEE']
                    },
                }
            }
        }

    