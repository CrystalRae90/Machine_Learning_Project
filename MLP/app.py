from flask import Flask, render_template, url_for, request
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import numpy as np
from keras.utils import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
import os
from keras.preprocessing import image

app = Flask(__name__)
model = load_model("model/bird_model.h5")
target_img = os.path.join(os.getcwd() , "static/test_images")

@app.route("/")
def index_view():
	return render_template("index.html")

#Allow files with extension png, jpg and jpeg
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXT

# Function to load and prepare the image in right shape
def read_image(filename):
    
    img = load_img(filename, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join("static/test_images", filename)
            file.save(file_path)
            img = read_image(file_path)
            class_prediction=model.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            print(classes_x)
            bird = (np.array_str(classes_x))
            return render_template("predict.html", bird = bird, prob=class_prediction, user_image = file_path)
        else:
            return "Unable to read the file. Please check file extension"


@app.route("/Our-Team")
def our_team():
	return render_template("Our-Team.html")

@app.route("/Model-Architecture")
def model_architecture():
    return render_template("Model-Architecture.html")

@app.route("/Project-Description")
def project_description():
	return render_template("Project-Description.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5500)
