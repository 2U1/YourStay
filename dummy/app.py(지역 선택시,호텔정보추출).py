import json
from bson.objectid import ObjectId
from operator import itemgetter
from flask import Flask
from pymongo import MongoClient
from flask import Flask,render_template,request,redirect,jsonify
from flask_pymongo import PyMongo
from flask import make_response
#from flask_jwt_extended.utils import get_jwt_identity

app=Flask(__name__)

app.config['JSON_AS_ASCII'] = False
#app.config['MONGO_DBNAME']='database'
app.config["MONGO_URI"]="mongodb+srv://NLP:likelion@likelion.hppms.mongodb.net/NLP"
mongo = PyMongo(app)
db=mongo.db

@app.route("/api/v1/juso",methods=['GET'])
def hotelnamejuso():
    return render_template('juso.html')

@app.route('/api/v1/byjuso', methods=['GET'])
def get_hotel_by_juso():

    juso = request.args.get("juso")
    hotels = db.hotel
    output = []
    for h in list(hotels.find()):
        if juso in h["hotelAddr"]:
            output.append({'hotel':h['hotelName'], 'addr':h['hotelAddr'], 'cleanliness':h['cleanliness'], 'convenience':h['convenience'], 'kindness':h['kindness'], 'position':h['position'], 'score':h['totalScore']})
    
    return jsonify({'result':output})
    #return render_template('juso.html',jsonify({'result':output}))
