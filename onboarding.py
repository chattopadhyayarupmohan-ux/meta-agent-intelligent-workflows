import requests

def create_customer(name: str, email: str):
    """
    Creates a new customer in the CRM system.
    """
    response = requests.post(
        "https://your-api-id.execute-api.region.amazonaws.com/prod/onboarding",
        json={
            "name": name,
            "email": email
        }
    )
    return response.json()
