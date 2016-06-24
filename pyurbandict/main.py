import requests

UD_GET_URL = "http://api.urbandictionary.com/v0/define"
UD_RANDOM_URL = "http://api.urbandictionary.com/v0/random"


class Model:
    def __init__(self, keyword=None):
        # TODO: logic for when keyword is None
        self.keyword = keyword
        r = requests.get(UD_GET_URL, params={'term': self.keyword})
        self.link = r.url
        self.data, self.status_code = r.json(), r.status_code
        self.exists = False if self.data[
            'result_type'] == 'no_results' else True

    def get_tags(self):
        pass

    def __repr__(self):
        return "Definitions for: {}".format(self.keyword)


if __name__ == '__main__':
    print(Model('acid').get_data()['tags'])
