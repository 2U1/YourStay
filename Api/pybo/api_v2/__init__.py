from os import access
from pybo.extensions import bcrpyt, jwt, cors
import bcrypt
from dns import message
from flask import Flask, request, Response, jsonify, redirect, url_for, make_response
import json
from flask_jwt_extended.utils import get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from operator import itemgetter
from flask_cors import CORS, cross_origin
from flask import Blueprint



def create_app():
    app=Flask(__name__)
    
    app.config["JWT_SECRET_KEY"] = "YourStay"
    app.config["CORS_HEADERS"] = 'Content-Type'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    jwt.init_app(app)
    cors.init_app(app)
    bcrpyt.init_app(app)
    
    from .api_v2 import reviews, hotels, login, register, recommended
    app.register_blueprint(login.bp)
    app.register_blueprint(register.bp)
    app.register_blueprint(reviews.bp)
    app.register_blueprint(hotels.bp)
    app.register_blueprint(recommended.bp)
    
    return app


if __name__ == "__main__":
    app.run(host='0.0.0.0')
