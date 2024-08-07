from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load pre-trained model
model = tf.keras.models.load_model(r"E:\project\my_model.h5")

# Define function to preprocess images
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalization
    return img_array

# Define route for file upload
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        
        file = request.files["file"]
        
        if file.filename == "":
            return "No selected file"
        
        if file:
            file_path = "temp.jpg"  # Save the file temporarily
            file.save(file_path)
            # Preprocess the uploaded image
            img_array = preprocess_image(file_path)
            # Perform prediction
            prediction = model.predict(img_array)
            # You may need to customize the response based on your model's output
            if prediction[0][0] > 0.5:
                result = "Tuberculosis detected"
            else:
                result = "Normal"
            
            return result
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
