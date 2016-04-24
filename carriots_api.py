from datetime import datetime
import requests
from time import mktime, sleep


class CarriotsApi:

    def __init__(self, api_key, device_id):
        self.api_key = api_key
        self.device_id = device_id
        self.url = 'https://api.carriots.com/streams/'


    def get_time(self):
        return int(mktime(datetime.now().timetuple()))


    def get_headers(self):
        return {'Carriots.apikey': self.api_key}


    def get_payload(self, data):
        payload = {
            "protocol": "v2",
            "at": self.get_time(),
            "device": self.device_id,
            "data": data,
            "checksum":""
        }
        return payload


    def post(self, data):
        r = requests.post(self.url,
                    headers=self.get_headers(),
                    json=self.get_payload(data))

        print(str(r.status_code) + ": " + r.reason)
        if(not r.ok):
            print(r.text)


if __name__ == "__main__":
    api_key = '1234567890abcdefghijklmnopqrstuvwxyz'
    device_id= 'defaultDevice@example.example'
    data = {"key1": "val1","key2": "val2"}

    c = CarriotsApi(api_key, device_id)
    c.post(data)
    sleep(15)
