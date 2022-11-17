from flask import render_template
from path import Path
import os, io
# from google.api_core.protobuf_helpers import get_messages
from google.cloud import vision
from collections.abc import Mapping


def process():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'peppy-booth-292312-3268e68a2665.json'
    client = vision.ImageAnnotatorClient()

    FOLDER_PATH = r'D:\pythonProject\major_project_final\data'
    IMAGE_FILE = 'Pen.jpg'
    FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)

    docText = response.full_text_annotation.text
    print(docText)

    with open('major.txt', 'w') as f:
        f.write(docText)
    return render_template('index.html')
