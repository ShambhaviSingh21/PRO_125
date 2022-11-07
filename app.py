#Import flask, jsonify and requests from flask to the file.
from flask import Flask, jsonify, request
from classifier import  get_prediction
#Create a flask app.
app = Flask(__name__)
#Write a route with an end point predict-alphabet and POST method.
@app.route("/predict-alphabet", methods=["POST"])
#Define a predict_data function.
def predict_data():
  image = request.files.get("digit")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app.run(debug=True)
