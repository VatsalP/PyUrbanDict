#!/usr/bin/env python3
import requests

UD_GET_URL = "http://api.urbandictionary.com/v0/define"
UD_RANDOM_URL = "http://api.urbandictionary.com/v0/random"


class Word:
    def __init__(self, keyword=None):
        # TODO: logic for when keyword is None
        if keyword:
            self.set_keyword(keyword)
        else:
            self.keyword = None

    def set_keyword(self, keyword):
        self.keyword = keyword
        r = requests.get(UD_GET_URL, params={'term': self.keyword})
        self.link = r.url
        self.data, self.status_code = r.json(), r.status_code
        self.exists = False if self.data[
            'result_type'] == 'no_results' else True

    def get_tags(self):
        """    Returns a list object containing all
               the tags.
        """
        if self.keyword:
            return self.data['tags']

    def get_definitions(self):
        """    Returns a list object containing all
               the definitions for the given keyword.
        """
        if self.keyword:
            return self.data['list']

    def get_sound(self):
        """    Returns a list object containing the
               urls of the sounds for the given keyword.
        """
        if self.keyword:
            return self.data['sounds']

    def __repr__(self):
        return "Definitions for: {}".format(self.keyword)


if __name__ == '__main__':
    m = Word('acid')
    print(m.get_definitions())
