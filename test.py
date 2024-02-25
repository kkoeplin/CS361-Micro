import requests

# valid body parts
valid_body_parts = [
    'back', 'cardio', 'chest', 'lower arms', 'lower legs', 
    'neck', 'shoulders', 'upper arms', 'upper legs', 'waist'
]

# URL of your microservice endpoint
url = 'http://localhost:5013/get_random_exercise'

while True:
    # Get the body part input from the user
    body_part = input("Enter one of the following body parts: " + ", ".join(valid_body_parts) + ": ").lower()

    # Check if the input valid
    if body_part in valid_body_parts:
        # Add the body part 2 the URL as a query parameter for a GET request
        request_url = f"{url}?bodyPart={body_part}"

        print("Sending request to:", request_url)

        # GET request to the microservice
        response = requests.get(request_url)

        try:
            data = response.json()
            # Print the received response
            print("Workout for", body_part, ":", data)
        except Exception as e:
            # print the error if failed
            print("Error decoding JSON:", e)

    else:
        print("Invalid input. Give it another try!")
        continue

    # Prompt the user to enter another body part
    choice = input("Do you want to enter another body part? yes or no?: ").lower()
    if choice != 'yes':
        break
