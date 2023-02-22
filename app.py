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
model = load_model("model/bird_modelv6.h5")
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
            if classes_x == 0:
                bird = "American Crow"
                facts = "A smart and adaptable bird that thrives in many habitats across North America--from forests to cities--the American Crow has a loud and distinctive caw that it uses to communicate with other crows, and can also mimic other sounds, such as car alarms and human voices."
            elif classes_x == 1:
                bird = "American Kestrel"
                facts = "North America's littlest falcon, the American Kestrel packs a predator's fierce intensity into its small body. It's one of the most colorful of all raptors: the male's slate-blue head and wings contrast elegantly with his rusty-red back and tail; the female has the same warm reddish on her wings, back, and tail."
            elif classes_x == 2:
                bird = "American Robin"
                facts = "A migratory bird of the true thrush genus and Turdidae--the wider thrush family--the American robin is named after its European counterpart because of its reddish-orange breast, though the two species are not closely related, with the European robin belonging to the Old World flycatcher family."
            elif classes_x == 3:
                bird = "Blue Jay"
                facts = "One of the most common backyard birds, blue jays have white underparts, blue upperparts, a blue crest, a black necklace, eye line, and bill, a blue tail with dark bars and a white bar and flecking on its wings. Both male and females look alike."
            elif classes_x == 4:
                bird = "Carolina Chickadee"
                facts = "Living in milder climates, carolina chickadees has been reported to be less of a visitor to bird feeders, but it does come into suburban yards for sunflower seeds. Where the ranges of Black-capped and Carolina chickadees come together, they often interbreed. In these contact zones, they also can learn to imitate each other's songs--causing great confusion for birdwatchers."
            elif classes_x == 5:
                bird = "Carolina Wren"
                facts = "Though this bird can be hard to see, it delivers an amazing number of decibels for its size. Follow its teakettle-teakettle! and other piercing exclamations through backyard or forest, and you may be rewarded with glimpses of this bird's rich cinnamon plumage, white eyebrow stripe, and long, upward-cocked tail. This hardy bird has been wintering farther and farther north in recent decades."
            elif classes_x == 6:
                bird = "Common Grackle"
                facts = "Grackles are blackbirds that look like they've been slightly stretched. They're taller and longer tailed than a typical blackbird, with a longer, more tapered bill and glossy-iridescent bodies. Grackles walk around lawns and fields on their long legs or gather in noisy groups high in trees, typically evergreens. They eat many crops (notably corn) and nearly anything else as well, including garbage."
            elif classes_x == 7:
                bird = "Eastern Pheobe"
                facts = "Despite its plain appearance, this flycatcher is often a favorite among eastern birdwatchers. It is among the earliest of migrants, bringing hope that spring is at hand. Seemingly quite tame, it often nests around buildings and bridges where it is easily observed. Best of all, its gentle tail-wagging habit and soft fee-bee song make the Phoebe easy to identify, unlike many flycatchers."
            elif classes_x == 8:
                bird = "European Starling"
                facts = "First brought to North America by Shakespeare enthusiasts in the nineteenth century, European Starlings are now among the continent's most numerous songbirds. They are stocky black birds with short tails, triangular wings, and long, pointed bills. Though they're sometimes resented for their abundance and aggressiveness, they're still dazzling birds when you get a good look. Covered in white spots during winter, they turn dark and glossy in summer."
            elif classes_x == 9:
                bird = "Great Blue Heron"
                facts = "The largest of the North American herons, they stand tall over wetlands and shores of open water. You can see these birds hanging out near the Buffalo Bayou."
            elif classes_x == 10:
                bird = "Great Egret"
                facts = "The wings of the great egret are proportionately longer and broader than most other white herons. In flight, the great egret holds its neck in a more open S-shape than do other white herons. The species utters a loud, low-pitched, hoarse croak. The sexes are similar in appearance but males are slightly larger."
            elif classes_x == 11:
                bird = "Northern Flicker"
                facts = "A large woodpecker with an overall brownish appearance, you will most likely find this bird in The Woodlands."
            elif classes_x == 12:
                bird = "Northern Mockingbird"
                facts = "These slender-bodied gray birds apparently pour all their color into their personalities. They sing almost endlessly, even sometimes at night, and they flagrantly harass birds that intrude on their territories, flying slowly around them or prancing toward them, legs extended, flaunting their bright white wing patches."
            elif classes_x == 13:
                bird = "Rock Pigeon"
                facts = "The rock dove, rock pigeon, or common pigeon is a member of the bird family Columbidae. In common usage, it is often simply referred to as the 'pigeon'. The domestic pigeon descended from this species. Escaped domestic pigeons have increased the populations of feral pigeons around the world."
            elif classes_x == 14:
                bird = "Snowy Egret"
                facts = "The snowy egret is a small white heron. The genus name comes from Provençal French for the little egret, aigrette, which is a diminutive of aigron, 'heron'. The species name thula is the Araucano term for the black-necked swan, applied to this species in error by Chilean naturalist Juan Ignacio Molina in 1782."
            else:
                bird = "Tufted Titmouse"
                facts = "A small songbird from North America, a species in the tit and chickadee family, this black-crested titmouse, found from central and southern Texas southward, was included as a subspecies but now is considered a separate species, Baeolophus atricristatus."
            #bird = (np.array_str(classes_x))
            return render_template("predict.html", bird = bird, facts = facts, user_image = file_path)
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
