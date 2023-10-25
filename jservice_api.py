import requests


def get_question(quantity:int):
    questions = requests.get('https://jservice.io/api/random', params={"count": f"{quantity}"}).json()
    return questions