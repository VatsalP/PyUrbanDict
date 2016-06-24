import requests

UD_GET_URL = "http://api.urbandictionary.com/v0/define?term="
UD_RANDOM_URL = "http://api.urbandictionary.com/v0/random"


class Model:

    def __init__(self, keyword=None):
        # TODO: logic for when keyword is None
        self.keyword = keyword
        self.link = UD_GET_URL + self.keyword


    def get_data(self):
        r = requests.get(self.link)
        return r.json()

    def get_tags(self):
        pass


if __name__ == '__main__':
    print(Model('acid').get_data()['tags'])

