from flask import Flask,request, jsonify
from transformers import pipeline
from sys import platform
import os

if platform == "linux" or platform == "linux2":
    os.system("pip3 install -q torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu")
elif platform == "win32" or platform == "darwin":
    os.system("pip3 install -q torch torchaudio torchvision")

os.system("pip install -q -r requirements.txt")
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

app = Flask(__name__)

@app.route("/", methods=['POST'])
def clasify():
    request_data = request.get_json()
    sequence = request_data['sequence']
    candidate = request_data['candidates']
    output = classifier(sequence, candidate, multi_label=True)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
