import requests

dummy_data = [
    {"user": "John", "email": "john@example.com", "input": "Dummy input 1"},
    {"user": "Alice", "email": "alice@example.com", "input": "Dummy input 2"},
    {"user": "Bob", "email": "bob@example.com", "input": "Dummy input 3"},
    {"user": "Emma", "email": "emma@example.com", "input": "Dummy input 4"},
    {"user": "Michael", "email": "michael@example.com", "input": "Dummy input 5"}
]

# This should be our body 
# {"email": "email@email.com"}
# This should be our response 
# { "input": "dummy"}

def insert_dummy_data():
    # try:
        # # Define the API endpoint URL
    api_url = "http://localhost:3000/test"        
        
    get_request = requests.get(api_url)

    

        # Iterate over dummy data and send POST requests
    #     for data in dummy_data:

    #         api_url = "http://localhost:8080/" + data["email"]
    #         input_data = { "input": data["input"]}
    #         # Send a POST request to the API endpoint
    #         response = requests.post(api_url, json=input_data)

    #         # Check if the request was successful
    #         if response.status_code == 200:
    #             print("Data inserted successfully.")
    #         else:
    #             print("Failed to insert data. Server responded with status code:", response.status_code)

    # except Exception as e:
    #     print("Failed to insert data:", e)

if __name__ == "__main__":
    insert_dummy_data()
