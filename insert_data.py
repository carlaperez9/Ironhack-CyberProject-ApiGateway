import requests
import time

dummy_data = [
    {"user": "John", "email": "john@example.com", "input": "Dummy input 1"},
    {"user": "Alice", "email": "alice@example.com", "input": "Dummy input 2"},
    {"user": "Bob", "email": "bob@example.com", "input": "Dummy input 3"},
    {"user": "Emma", "email": "emma@example.com", "input": "Dummy input 4"},
    {"user": "Michael", "email": "michael@example.com", "input": "Dummy input 5"}
]

dummy_inputs = [
    {"input": "SELECT * FROM users"},
    {"input": "Test input 2"},
    {"input": "Test input 3"},
    {"input": "UPDATE users SET input='TEST12345' WHERE id=2"},
    {"input": "Test input 1"}
]

def set_intervals(dummy_inputs): 
    for data in dummy_inputs: 
        # send data every x seconds 
        patch_dummy_data()

def get_dummy_data(): 

    api_url = "http://54.221.31.68:3000/test"

    get_request = requests.get(api_url)

    # Check if the request was successful
    if get_request.status_code == 200:
        list_of_emails = []
        data = get_request.json()['data']
        print("Data:", data)

        for user_data in data:
            email = user_data['email']
            list_of_emails.append(email)
        return list_of_emails
    else:
        print("Failed to insert data. Server responded with status code:", get_request.status_code)
        return []

def insert_dummy_data():
    # Iterate over dummy data and send POST requests
    for data in dummy_data:
        api_url = "http://54.221.31.68:3000/" + data["email"]
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

    index = 0

    for email in existing_emails:
        api_url = "http://54.221.31.68:3000/" + email
        response = requests.patch(api_url, json=dummy_inputs[index % len(dummy_inputs)])
        
        if response.status_code == 200:
            data = response.json()
            print("Updated input data for:", email, ":", data)
        else:
            print("Failed to update input data for", email, response.status_code)
        index += 1
        time.sleep(3)

if __name__ == "__main__":
    print("------------ PRIOR TO PATCH ------------")
    existing_emails = get_dummy_data()
    patch_dummy_data(existing_emails)
    print("------------ AFTER PATCH --------------")
    get_dummy_data()
    # insert_dummy_data()
