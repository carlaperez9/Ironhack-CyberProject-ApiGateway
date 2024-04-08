import requests
import time

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

def get_dummy_data(): 

    api_url = "http://localhost:3000/test"

    get_request = requests.get(api_url)

    # Check if the request was successful
    if get_request.status_code == 200:
        data = get_request.json()
        print("Data:", data)

        if 'emails' in data:
            emails = [item['email'] for item in data]
            print("Emails:", emails)
            return emails
        else:
            print("No emails found in the data.")
            return []
    else:
        print("Failed to insert data. Server responded with status code:", get_request.status_code)
        return []

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

def patch_dummy_data(existing_emails):
    
    dummy_inputs = [
        {"input": "SELECT * FROM users"},
        {"input": "Test input 1"},
        {"input": "Test input 2"},
        {"input": "UPDATE users SET input='TEST12345' WHERE id=1"},
        {"input": "Test input 3"}
    ]

    for email in existing_emails:
        api_url = "http://localhost:3000/" + email
        response = requests.patch(api_url, json=dummy_inputs)

    if response.status_code == 200:
        data = response.json()
        print("Updated input data for:", email, ":", data)
    else:
        print("Failed to update input data for", email, response.status_code)

if __name__ == "__main__":
    existing_emails = get_dummy_data()
    patch_dummy_data(existing_emails)
    # insert_dummy_data()
