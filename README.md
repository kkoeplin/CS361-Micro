# CS361-Microservice Project (Fitness App)

# Communication Contract
This microservice will provide a random workout based on a body part the user would like to target.
  1) Ensure that the microservice is running and accessible at http://localhost:5013/get_random_exercise.

## How to REQUEST data from the microservice:

To request data from the microservice, follow these steps:

1) Establish a connection between the client and the microservice by sending a GET request to the microservice endpoint.

  Example URL: http://localhost:5013/get_random_exercise

2) Include the desired body part as a query parameter in the request URL. Valid body part inputs include:

  'back'
  'cardio'
  'chest'
  'lower arms'
  'lower legs'
  'neck'
  'shoulders'
  'upper arms'
  'upper legs'
  'waist'
  
  If an invalid input is provided, the user will be prompted to try another input.

3) Upon receiving a valid input, the microservice will forward the request to an external API.

4) The external API will respond with data containing 10 random exercises based on the specified body part.

5) The microservice will randomly select one exercise from the received data and send it back as a response to the client.

6) The client will receive the chosen exercise as the response.

Example:
import requests
url = 'http://localhost:5013/get_random_exercise'
body_part = 'upper arm'
request_url = f"{url}?bodyPart={body_part}"
response = requests.get(request_url)
print("Exercise:", response.json())

7) The user will be prompted to input another body part after receiving the response.
   
## Receiving Data:

Example:

  

## UML Sequence Diagram
