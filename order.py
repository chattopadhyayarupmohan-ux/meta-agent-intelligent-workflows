import requests

def create_order(product: str, quantity: int):
    """
    Creates a new product order in the system.
    """
    response = requests.post(
        "https://your-api-id.execute-api.region.amazonaws.com/prod/order",
        json={
            "product": product,
            "quantity": quantity
        }
    )
    return response.json()
