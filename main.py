import requests

key = input("Enter your api key here: ")
model = input("What is the username of the shape that you want to talk to (please DON'T include the @): ")

def askshapes():
    message = input("Write your message here: ")

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": f"shapesinc/{model}",
        "messages": [{ "role": "user", "content": message }]
    }

    result = requests.post("https://api.shapes.inc/v1/chat/completions", headers=headers, json=body)
    data = result.json()
    # Print the assistant's reply if present
    try:
        print(data["choices"][0]["message"]["content"])
    except (KeyError, IndexError):
        print("Error: Unexpected response format:", data)

while True:
    askshapes()