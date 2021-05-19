from flask import Flask, jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://NLP:likelion@likelion.hppms.mongodb.net/'
app.config['MONGO_DBNAME'] = 'NLP'

mongo = PyMongo(app)

@app.route('/list')
def get_hotel_list():
    hotels = mongo.db.tokenized_review
    output = []

    hotel_list = hotels.find().distinct('hotelName')