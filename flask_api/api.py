from flask import Flask, request,jsonify
from load_models import load_models
from predict_rating import predict_rating
from load_cuisines import load_cuisines
from flask_cors import CORS,cross_origin


app = Flask(__name__)

already_loaded={}# stores models which are already loaded
cuisines=load_cuisines()

@app.route("/", methods=['POST'])
@cross_origin(origin="*")
def api():
    model=load_models(already_loaded,request.json['model'])
    rating= predict_rating(model,request.json,cuisines)
    response= jsonify({"rating":str(rating[0])})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run(debug=True)