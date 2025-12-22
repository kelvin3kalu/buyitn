import requests
from django.conf import settings

def get_paypal_access_token():
    url = f"{settings.PAYPAL_BASE_URL}/v1/oauth2/token"

    response = requests.post(
        url,
        auth=(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET),
        data={"grant_type": "client_credentials"},
    )

    response.raise_for_status()
    return response.json()["access_token"]


def create_paypal_order(total):
    access_token = get_paypal_access_token()

    url = f"{settings.PAYPAL_BASE_URL}/v2/checkout/orders"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    data = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": "GBP",
                    "value": str(total),
                }
            }
        ],
        "application_context": {
            "return_url": "http://127.0.0.1:8000/paypal/capture/",
            "cancel_url": "http://127.0.0.1:8000/cart/",
        },
    }

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()

    result = response.json()

    approval_url = next(
        link["href"] for link in result["links"] if link["rel"] == "approve"
    )

    return {
        "id": result["id"],
        "approval_url": approval_url,
    }


def capture_paypal_order(order_id):
    access_token = get_paypal_access_token()

    url = f"{settings.PAYPAL_BASE_URL}/v2/checkout/orders/{order_id}/capture"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(url, headers=headers)
    response.raise_for_status()

    return response.json()
