from flask import Flask, request
from load_models import load_models
from predict_rating import predict_rating
from load_cuisines import load_cuisines

app = Flask(__name__)

already_loaded={}# stores models which are already loaded
cuisines=load_cuisines()

@app.route("/", methods=['POST'])
def api():
    model=load_models(already_loaded,request.json['model'])
    rating= predict_rating(model,request.json,cuisines)
    return {'rating':str(rating[0])}


app.run(debug=True)