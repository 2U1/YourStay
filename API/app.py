from os import access
import bcrypt
from dns import message
from flask import Flask, request, Response, jsonify, redirect, url_for
import json
from flask_jwt_extended.utils import get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from operator import itemgetter


app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://NLP:likelion@likelion.hppms.mongodb.net/NLP'
app.config["JWT_SECRET_KEY"] = "YourStay"
# app.config['MONGO_DBNAME'] = 'NLP'

mongo = PyMongo(app)
bcrpyt = Bcrypt(app)
jwt = JWTManager(app)

db = mongo.db


@app.route('/api/v1/register', methods=['POST'])
def register():
    user_id = request.form['userid']
    user_name = request.form['username']
    password = request.form['password']
    clean = request.form['clean']
    conv = request.form['conv']
    kind = request.form['kind']
    position = request.form['position']



    if db.user.find_one({'user_id':user_id}):
        return jsonify(message='ID Already Exist')

    else:
        hased = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {'user_id':user_id, 'password':hased, 'user_name':user_name, 'cleanliness':int(clean), 'convenience':int(conv), 'kindness':int(kind), 'position':int(position) }
        db.user.insert_one(user_data)

        return jsonify(message='User Registered')


@app.route('/api/v1/login', methods=['POST'])
def login():
    if request.is_json:
        user_id = request.json['userid']
        password = request.json['password']
    else:
        user_id = request.form['userid']
        password = request.form['password']

    
    user_info = db.user.find_one({'user_id':user_id})

    if not user_info:
        return jsonify(message='No User')

    else:
        id_val = user_info['user_id']
        pwcheck = user_info['password']
        
        if bcrypt.checkpw(password.encode('utf-8'), pwcheck):
            access_token = create_access_token(identity=id_val)

            return jsonify(message="Logged In", access_token=access_token)

        else:
            return jsonify(message="No verified email or password")



@app.route('/api/v1/hotels', methods=['GET'])
def get_hotel():
    hotels = db.hotel
    output = []
    for h in hotels.find():
        output.append({'name':h['hotelName'], 'cleanliness':h['cleanliness'], 'convenience':h['convenience'], 'kindness': h['kindness'], 'position':h['position'], 'score':h['totalScore'], 'id':h['hotel_id']})

    return jsonify({'result':output})



@app.route('/api/v1/hotels/recommended', methods=['GET'])
@jwt_required()
def recommend_hotel():
    hotels = db.hotel
    users = db.user
    
    current_user = get_jwt_identity()
    user_info = users.find_one({'user_id':current_user})
    user_scores = {'cleanliness':user_info['cleanliness']*0.1, 'position':user_info['position']*0.1, 'convenience': user_info['convenience']*0.1, 'kindness':user_info['kindness']*0.1}

    hotel_infos = list(hotels.find())

    weighted_scores = []

    for h in hotel_infos:
        weighted = {}
        weighted['name'] = h['hotelName']
        weighted['score'] = (user_scores['cleanliness']*h['cleanliness'] + user_scores['position']*h['position'] + user_scores['convenience']*h['convenience'] + user_scores['kindness']*h['kindness']) / 4
        weighted_scores.append(weighted)

    
    recommended = sorted(weighted_scores, key = itemgetter('score'), reverse=True)[0:5]

    return jsonify({'result':recommended})
    

@app.route('/api/v1/hotels/reviews/<int:hotelid>', methods=['GET'])
def get_review(hotelid):
    reviews = db.tokenized_review
    hotel = db.hotel
    keyword = db.keyword

    hotel_doc = hotel.find_one({'hotel_id':hotelid})
    del hotel_doc['_id']

    keyword_doc = keyword.find({'hotel_id':hotelid})

    keyword_output = []

    for k in keyword_doc:
        keyword_info = {'rep':k['rep']}

        k_list = k['keywords']

        review_content = []
        review_ids = []

        pos_count = 0
        neg_count = 0

        for w in k_list:
            for r in reviews.find({'hotel_id':hotelid,'tokens':w}):
                if r['label'] == 0:
                    neg_count += 1
                elif r['label'] == 1:
                    pos_count += 1

                if r['reviewID'] not in review_ids:
                    keyword_reviews = {'id':r['reviewID'], 'content':r['content']}
                    review_content.append(keyword_reviews)
                    review_ids.append(r['reviewID'])
                    
        keyword_info['pos'] = pos_count
        keyword_info['neg'] = neg_count
        keyword_info['reviews'] = review_content


        keyword_output.append(keyword_info)

    return jsonify({'hotel':hotel_doc, 'review':keyword_output})

    


if __name__ == "__main__":
    app.run(debug=True)