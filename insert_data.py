import requests

def insert_data(user, email, input_data):
    try:
        # Define the API endpoint URL
        api_url = "http://your_ec2_instance_ip:your_nodejs_api_port/insert"

        # Define the JSON payload to send
        payload = {
            "user": user,
            "email": email,
            "input": input_data
        }

        # Send a POST request to the API endpoint
        response = requests.post(api_url, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            print("Data inserted successfully.")
        else:
            print("Failed to insert data. Server responded with status code:", response.status_code)

    except Exception as e:
        print("Failed to insert data:", e)

if __name__ == "__main__":
    # Example usage
    user = input("Enter user: ")
    email = input("Enter email: ")
    input_data = input("Enter input: ")

    insert_data(user, email, input_data)
