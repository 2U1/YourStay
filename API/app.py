from flask import Flask, request, Response, jsonify
import json
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://NLP:likelion@likelion.hppms.mongodb.net/NLP'
# app.config['MONGO_DBNAME'] = 'NLP'

mongo = PyMongo(app)

db = mongo.db

@app.route('/api/v1/hotels', methods=['GET'])
def get_hotel():
    hotels = db.hotel
    output = []
    for h in hotels.find():
        output.append({'name':h['hotelName'], 'cleanliness':h['cleanliness'], 'convenience':h['convenience'], 'kindness': h['kindness'], 'position':h['position'], 'score':h['totalScore'], 'id':h['hotel_id']})

    return jsonify({'result':output})

@app.route('/api/v1/hotels/<hotel_id>')
def get_info(hotel_id):
    tokenized = db.tokenized_review
    output = []
    info = tokenized.find({'hotel_id':hotel_id})
    



if __name__ == "__main__":
    app.run()