from flask import Flask,request, jsonify
from transformers import pipeline
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
