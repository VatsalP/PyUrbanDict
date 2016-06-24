import requests

UD_GET_URL = "http://api.urbandictionary.com/v0/define?term="
UD_RANDOM_URL = "http://api.urbandictionary.com/v0/random"


class Model:
    def __init__(self, keyword=None):
        # TODO: logic for when keyword is None
        self.keyword = keyword
        self.link = UD_GET_URL + self.keyword
        r = requests.get(self.link)
        self.data = r.json()
        self.status = r.status_code

    def get_tags(self):
        pass


if __name__ == '__main__':
    print(Model('acid').get_data()['tags'])
