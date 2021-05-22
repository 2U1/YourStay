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

#@app.route("/")
@app.route("/api/v1/hotels",methods=['GET'])
def hotelnameinput():
    return render_template('base.html')

#@app.route("/api/v1/hotels/<int:hotel_id>",methods=['GET'])
#무려 13~15초 걸림..
@app.route("/api/v1/hotelinfo",methods=['GET'])
def MongoTest():

    output=[]
    hotelid=request.args.get("hotel_id")
    
    keywords=db.keyword
    hotels=db.hotel
    tokens=db.tokenized_review
    hotels_list = db.hotel.find({'hotel_id':int(hotelid)},{'_id':0,'hotelName':1,'cleanliness':2,'convenience':3,'kindness':4,'position':5,'totalScore':6})
    tokens_list = db.tokenized_review.find({'hotel_id':int(hotelid)})

    keywords_list = list(db.keyword.find({"hotel_id":int(hotelid)},{'_id':0,'keywords':1,'rep':2, 'hotelName':3}))
        

    for i in keywords_list:
        diction={}
        for j in i['keywords']:
            for document in (list(db.tokenized_review.find({'hotel_id':int(hotelid),"tokens":{"$in":[j]}}))):
                if document['_id'] in diction.keys():
                    diction[document['_id']]=diction[document['_id']]+1
                else:
                    diction[document['_id']]=0
        reverse=sorted(diction.items(),reverse=True, key=lambda item: item[1])
        output.append({'hotelName':hotels_list[0]['hotelName'],'cleanliness':hotels_list[0]['cleanliness'], 'convenience':hotels_list[0]['convenience'], 'kindness': hotels_list[0]['kindness'], 'position':hotels_list[0]['position'], 'represent':i['rep'],'content':db.tokenized_review.find_one({'hotel_id':int(hotelid),'_id': ObjectId(str(reverse[0][0]))},{'_id':0,'content':1})['content'],'label':db.tokenized_review.find_one({'hotel_id':int(hotelid),'_id': ObjectId(str(reverse[0][0]))},{'_id':0,'label':1})['label']})
        
    return jsonify({'result':output})
