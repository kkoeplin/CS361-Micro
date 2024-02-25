import random
import requests
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

RAPIDAPI_HOST = "exercisedb.p.rapidapi.com"
RAPIDAPI_KEY = '7765a9f05cmshfd96333e49c88c8p144dcfjsn8f77e4b99e76'

@app.route('/get_random_exercise')
def get_random_exercise():
    body_part = request.args.get('bodyPart')
    if not body_part:
        print("Error: Body part parameter is required.")
        return jsonify({"error": "Body part parameter is required."}), 400
    
    print(f"Request received for body part: {body_part}")
    time.sleep(1) 

    # Gets t10 diff exercises based on the body part recieved form UI
    url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{body_part}?limit=10"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    
    try:
        print("Sending request to external API...")
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        data = response.json()
        if data:
            print("Data received from external API.")
            # of the ten pick a random one so not the same every time
            random_exercise = random.choice(data)
            time.sleep(1)  
            print("Sending random exercise as response.")
            return jsonify(random_exercise)
        else:
            print("No exercise data received from API.")
            return jsonify({"error": "Failed to retrieve exercise for that body part."}), 500
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    print("Microservice running...") 
    app.run(port=5013)
