import os
import sys

import pytest

sys.path.append('../src')
from src.carriots_api import CarriotsApi


def test_bad_api_key():
    api_key = '1234567890abcdefghijklmnopqrstuvwxyz'
    device_id= 'defaultDevice@example.example'
    data = {"test_key 1": "test_val 1","test_key 2": "test_val 2"}

    c = CarriotsApi(api_key, device_id)
    c.send_stream(data)
    assert c.status == {"response": "Not authorized: apikey not found"}


def test_send_stream():
    api_key = os.environ.get('CARRIOTS_KEY')
    device_id = os.environ.get('CARRIOTS_ID')
    data = {"test_key 1": "test_val 1","test_key 2": "test_val 2"}

    c = CarriotsApi(api_key, device_id)
    c.send_stream(data)
    assert c.status == {'response': 'OK'}


def test_send_status():
    api_key = os.environ.get('CARRIOTS_KEY')
    device_id = os.environ.get('CARRIOTS_ID')
    print(device_id)
    payload = {'battery': 42}

    c = CarriotsApi(api_key, device_id)
    c.send_status(payload)
    assert c.status == {'response': 'OK'}


if __name__ == '__main__':
    pytest.main()
