from flask import Flask, request, jsonify, render_template, send_from_directory
import tensorflow as tf
import numpy as np
from flask_cors import CORS

from routes_predicts import bp as predict_bp

app = Flask(__name__)
CORS(app)

# Register the routes Blueprints
app.register_blueprint(predict_bp)

# Define a route to serve the images
@app.route('/images/<path:filename>')
def get_image(filename):
    # Specify the path to your local image folder
    image_folder = './ImgResult'
    
    # Serve the image file from the specified folder
    return send_from_directory(image_folder, filename)


@app.route('/')
def handle_request():
    return 'Connected to Server'

@app.route('/DemoTeam14/slides')
def render_Slide():
    return render_template('Slides.html')


@app.route('/DemoTeam14')
def render_Demo():
    return render_template('DemoInternet.html')

# Run the application
if __name__ == '__main__':
    # change host to local IP address for hardware public request
    # app.run(host="172.20.10.3")
    app.run(host='0.0.0.0', port=5000)