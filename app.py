from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(filename='api_performance.log', level=logging.INFO)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    country = request.args.get('country', 'all')
    if country == 'all':
        prediction = {"Singapore": 150, "US": 200, "UK": 120}
    else:
        prediction = {country: 150}
        
    logging.info(f"Prediction requested for country: {country}")
    return jsonify({"country": country, "prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
