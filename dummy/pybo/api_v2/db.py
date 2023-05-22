from os import access
import bcrypt
from dns import message
from flask import Flask, request, Response, jsonify, redirect, url_for, Blueprint
import json
from flask_jwt_extended.utils import get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from operator import itemgetter
from flask_cors import CORS, cross_origin
app = Flask(__name__)

@app.before_request
def get_db():
    app.config['MONGO_URI'] = 'mongodb+srv://NLP:likelion@likelion.hppms.mongodb.net/NLP'

    mongo = PyMongo(app)
    db=mongo.db
    return db
