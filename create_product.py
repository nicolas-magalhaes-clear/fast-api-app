import requests
import json

# API endpoint
url = "http://localhost:8000/products"

# Product data
product_data = {
    "name": "Sample Product",
    "price": 99.99,
    "description": "This is a sample product description"
}

# Send POST request
response = requests.post(
    url,
    json=product_data,
    headers={"Content-Type": "application/json"}
)

# Print response
print(f"Status Code: {response.status_code}")
print("Response:")
print(json.dumps(response.json(), indent=2)) 