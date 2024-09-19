import requests
import random


category = random.choice([9, 12, 14, 15, 17, 18, 23])


class Data:
    """A module for requesting a random data set from the API and storing it in a json"""
    def __init__(self):
        parameters = {
            'amount': 10,
            'category': category,
            'difficulty': 'medium',
            'type': 'boolean'
        }
        quiz_api = "https://opentdb.com/api.php/json"
        response_code = requests.get(url=quiz_api, params=parameters)
        response_code.raise_for_status()
        self.q_data = response_code.json()['results']

