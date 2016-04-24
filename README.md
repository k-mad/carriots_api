# carriots_api
A simple python api for interacting with carriots

# Usage

Example post stream
-------------------
    from carriots_api import CarriotsApi

    client = CarriotsApi("YOUR APIKEY", "YOUR DEVICE_ID")
    data = {"KEY":"VALUE"}
    client.post(data)