#user details for org_360 project

def user_details_schema():
    return {
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['first_name', 'last_name', 'team', 'skills', 'user_name','email_id', 'mobile_number', 'grade'],
            'properties': {
                'first_name': {
                    'bsonType':'string'
                },
                'last_name': {
                    'bsonType':'string'
                },
                'team': {
                    'bsonType':'string',
                    'enum': ['FULL_STACK', 'FRONT_END', 'BACK_END', 'TESTING', 'DEVOPS', 'DATABASE']
                },
                'skills': {
                    'bsonType':'array'
                },
                'user_name': {
                    'bsonType': 'string'
                },
                'email_id': {
                    'bsonType': 'string'
                },
                'mobile_number': {
                    'bsonType': 'string'
                },
                'grade': {
                    'bsonType': 'string',
                    'enum': ['GRADE_A', 'GRADE_A+','GRADE_B', 'GRADE_C',]
                },
                'projects': {
                    'bsonType': 'string'
                }
            }
        }
    }