from flask import Flask, request, jsonify
import joblib
import pandas as pd
from THE_CODE import extract_features

app = Flask(__name__)

from flask_cors import CORS
CORS(app)

model = joblib.load('phishing_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    features = extract_features(url)
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]

    result = "Phishing" if prediction == 1 else "Legit"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
