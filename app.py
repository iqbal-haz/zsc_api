from flask import Flask,request, jsonify
from importlib.util import find_spec
from transformers import pipeline
from sys import platform
import re
import os

with open("requirements.txt", 'r') as f:
    for package in f.readlines():
        package = package.rstrip()
        punc = re.search(r'\W+', package)
        punc = punc.start() if punc else None
        pkg_name = package[:punc]

        if find_spec(pkg_name) is None:
            os.system(f"pip install {package}")

# if platform == "linux" or platform == "linux2":
#     os.system("pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu")
# elif platform == "win32" or platform == "darwin":
#     os.system("pip3 install torch torchaudio torchvision")

# os.system("pip install -r requirements.txt")
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
