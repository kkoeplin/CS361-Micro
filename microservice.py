import requests
import random # Use to get the random exercise
from flask import Flask, jsonify, request

app = Flask(__name__)

RAPIDAPI_HOST = "exercisedb.p.rapidapi.com"
RAPIDAPI_KEY = '7765a9f05cmshfd96333e49c88c8p144dcfjsn8f77e4b99e76'

@app.route('/get_random_exercise')
def get_random_exercise():
    body_part = request.args.get('bodyPart')
    if not body_part:
        return jsonify({"error": "Body part parameter is required."}), 400
    
    url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{body_part}?limit=10"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception
        data = response.json()
        if data:
            random_exercise = random.choice(data)
            return random_exercise
        else:
            return jsonify({"error": "Failed to retrieve exercise for the given body part."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5013)
