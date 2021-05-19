from flask import Flask, request, Response
import json
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://NLP:likelion@likelion.hppms.mongodb.net/'
app.config['MONGO_DBNAME'] = 'NLP'

mongo = PyMongo(app)

app.run()