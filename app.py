from flask import Flask, render_template, url_for, request, jsonify
import tensorflow as tf

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

# Load the saved model
#model = tf.saved_model.load("/content/drive/My Drive/bird_model.h5")

# @app.route("/predict", methods=["POST"])
# #def predict():
#     # Get the input data from the request
#     input_data = request.get_json()

#     # Use the model to make a prediction
#     prediction = model.predict(input_data)

#     # Return the prediction as a JSON response
#     return jsonify({"prediction": prediction.tolist()})


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
