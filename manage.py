from flask import Flask
from flask_jwt_extended import JWTManager
from config import SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES
import controller

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
jwt = JWTManager(app)

app.register_blueprint(controller.mod)

if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=8001)