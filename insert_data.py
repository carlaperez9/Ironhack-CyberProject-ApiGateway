import requests

dummy_data = [
    {"user": "John", "email": "john@example.com", "input": "Dummy input 1"},
    {"user": "Alice", "email": "alice@example.com", "input": "Dummy input 2"},
    {"user": "Bob", "email": "bob@example.com", "input": "Dummy input 3"},
    {"user": "Emma", "email": "emma@example.com", "input": "Dummy input 4"},
    {"user": "Michael", "email": "michael@example.com", "input": "Dummy input 5"}
]

# # make a post request of this? 
# dummy_inputs = [
#     {"input" : " 'SELECT * FROM users' "} 
#     # añadir inputs maliciosos 
# ]

# This should be our body 
# {"email": "email@email.com"}
# This should be our response 
# { "input": "dummy"}


def get_dummy_data(): 

    api_url = "http://localhost:3000/test"

    get_request = requests.get(api_url)

    # Check if the request was successful
    if get_request.status_code == 200:
        data = get_request.json()
        print("Data:", data)
    else:
        print("Failed to insert data. Server responded with status code:", get_request.status_code)
    
    print(get_request)

def insert_dummy_data():
    # Iterate over dummy data and send POST requests
    for data in dummy_data:
        api_url = "http://localhost:3000/" + data["email"]
        input_data = { "input": data["input"]}
    # Send a POST request to the API endpoint
        response = requests.post(api_url, json=input_data)

    if response.status_code == 200:
        data = response.json()
        print("Dummy data: ", data)
    else:
        print("Failed to insert data. Server responded with status code:", response.status_code)

    # except Exception as e:
    #     print("Failed to insert data:", e)

if __name__ == "__main__":
    get_dummy_data()
    # insert_dummy_data()
