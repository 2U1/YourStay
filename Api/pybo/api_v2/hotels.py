from os import access
#pybo폴더 안에 api_v2 폴더 안에 db.py가 존재하므로
from pybo.api_v2.db import get_db
import bcrypt
from dns import message
from flask import Flask, request, Response, jsonify, redirect, url_for, Blueprint,render_template
import json
from flask_jwt_extended.utils import get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from operator import itemgetter
from flask_cors import CORS, cross_origin

bp = Blueprint('hotel',__name__,url_prefix='/api/v2')

@bp.route('/hotels', methods=['GET'])
def get_hotel():
    db=get_db()
    region = request.args.get("region","all",str)
    
    hotels = db.hotel
    output = []

    if region == "all":
        for h in list(hotels.find()):
            del h['_id']
            output.append(h)
        return jsonify({'result':output})
    else:
        for h in list(hotels.find({"$text":{"$search":region}})):
            del h['_id']
            output.append(h)
        return jsonify({'result':output})
