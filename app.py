
from flask import Flask, render_template, request, Blueprint, url_for, send_file
import cv2
from path import Path
import os, io
# from google.api_core.protobuf_helpers import get_messages
from google.cloud import vision
from collections.abc import Mapping

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home_get():
    if request.method == 'POST':
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'peppy-booth-292312-3268e68a2665.json'
        client = vision.ImageAnnotatorClient()
        imagefile_2 = request.files['content']
        imagefile_2.save(f"static\images\content.jpeg")
        IMG = r'static\images\content.jpeg'
        with io.open(IMG, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)

        docText = response.full_text_annotation.text
        print(docText)

        with open('major.txt', 'w') as f:
            f.write(docText)
        f.close()
        return render_template('final.html')
    return render_template('index.html')


@app.route('/download')
def download():
    path = 'major.txt'
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
