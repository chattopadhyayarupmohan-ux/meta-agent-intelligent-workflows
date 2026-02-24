import requests

def create_customer(name: str, email: str):
    """
    Creates a new customer in the CRM system.
    """
    response = requests.post(
        "https://0m9rrsy307.execute-api.us-east-1.amazonaws.com/prod/onbaording",
        json={
            "name": name,
            "email": email
        }
    )
    return response.json()
