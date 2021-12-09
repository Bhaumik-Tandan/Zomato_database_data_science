from flask import Flask, request,jsonify
from load_models import load_models
from predict_rating import predict_rating
from load_cuisines import load_cuisines
from flask_cors import CORS

app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": ["*"]}})#for cross origin

already_loaded={}# stores models which are already loaded
cuisines=load_cuisines()

@app.route("/", methods=['POST'])
def api():
    model=load_models(already_loaded,request.json['model'])
    rating= predict_rating(model,request.json,cuisines)
    response= jsonify({"rating":str(rating[0])})
    return response


app.run(debug=True)

# fetch("http://localhost:5000 ", {
#          method: "POST",
#          body:JSON.stringify({
#              "model":"random_forest",
#              "longitude": 23,
#              "latitude": 43,
#              "average_cost_for_two": 200,
#              "has_table_booking": 1,
#              "has_online_delivery": 0,
#              "is_delivering_now": 1,
#              "switch_to_order_menu": 1,
#              "price_range": 1,
#              "votes": 300,
#              "cuisines": ["French", "Japanese", "Desserts", "Seafood"]
#          }),
#             headers: {
#                 "Content-Type": "application/json"
#             }
# });