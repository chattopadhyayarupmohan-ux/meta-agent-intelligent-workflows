import requests

def create_order(product: str, quantity: int):
    """
    Creates a new product order in the system.
    """
    response = requests.post(
        "https://0m9rrsy307.execute-api.us-east-1.amazonaws.com/prod/order",
        json={
            "product": product,
            "quantity": quantity
        }
    )
    return response.json()
