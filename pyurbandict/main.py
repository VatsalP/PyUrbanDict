#!/usr/bin/env python3
import requests

from . import exception

UD_GET_URL = "http://api.urbandictionary.com/v0/define"
UD_RANDOM_URL = "http://api.urbandictionary.com/v0/random"


class Word:
    def __init__(self, keyword=None):
        try:
            if keyword:
                self.keyword = keyword
                r = requests.get(UD_GET_URL, params={'term': self.keyword})
                self.link = r.url
                self.data, self.status_code = r.json(), r.status_code
                self.exists = False if self.data[
                    'result_type'] == 'no_results' else True
            else:
                raise exception.KeywordError
        except exception.KeywordError:
            print("\nKeywordError: No keyword is set.\n")

    def get_tags(self):
        """Returns a list object containing all
        the tags.
        """
        return self.data['tags']

    def get_definitions(self):
        """Returns a list object containing all
        the definitions for the given keyword.
        """
        return self.data['list']

    def get_sound(self):
        """Returns a list object containing the
        urls of the sounds for the given keyword.
        """
        return self.data['sounds']

    def __repr__(self):
        return "Definitions for: {}".format(self.keyword)


if __name__ == '__main__':
    m = Word('acid')
    print(m.get_definitions())
    m = Word()
