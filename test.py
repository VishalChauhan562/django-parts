import requests
import json

# Replace "" with your actual URL
Url = "http://127.0.0.1:8000/challenges/month-create/"

data = {"name": "Manasvi", "idea": "Vishal is cool", "position": 9, "isGoodIdea": True}

# No need to manually serialize the data, requests module will handle it
r = requests.post(url=Url, json=data)

# Check if request was successful
if r.status_code == 200:
    try:
        # Get the response data
        response_data = r.json()
        print(response_data)
    except json.decoder.JSONDecodeError as e:
        print(f"Failed to decode JSON response: {e}")
        print(f"Response content: {r.content}")
else:
    print(f"Request failed with status code {r.status_code}")
    print(f"Response content: {r.content}")
