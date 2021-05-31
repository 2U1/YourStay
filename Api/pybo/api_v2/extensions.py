from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash


jwt = JWTManager()
cors = CORS(resources={r"/": {"origins": "http://localhost:5000"}})
bcrpyt = Bcrypt()
