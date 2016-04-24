# carriots_api
A simple python api for interacting with carriots

# Usage

send stream example
-------------------
Used to send device info to carriots.

    from carriots_api import CarriotsApi

    client = CarriotsApi("YOUR APIKEY", "YOUR DEVICE_ID")
    data = {"KEY":"VALUE"}
    client.send_stream(data)

send status example
-------------------
Used to send device status info to carriots.

    from carriots_api import CarriotsApi

    client = CarriotsApi("YOUR APIKEY", "YOUR DEVICE_ID")
    data = {"KEY":"VALUE"}
    client.send_status(data)