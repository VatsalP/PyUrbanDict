#!/usr/bin/env python3
import requests

from . import exception

UD_GET_URL = "http://api.urbandictionary.com/v0/define"
UD_RANDOM_URL = "http://api.urbandictionary.com/v0/random"


class Word:
    """Urbandictionary api Wrapper

    :param keyword: the word whose definitions are to be found
    :type keyword: class:`str`
    """
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

    def get_data(self):
        """Returns a dict object containing everything

        :return: :class:`dict`
        """
        return self.data

    def get_tags(self):
        """Returns a list object containing all
        the tags.

        :return: :class:`list`
        """
        return self.data['tags']

    def get_definitions(self):
        """Returns a list object containing all
        the definitions for the given keyword.

        :return: :class:`list`
        """
        return self.data['list']

    def get_sound(self):
        """Returns a list object containing the
        urls of the sounds for the given keyword.

        :return: :class:`list`
        """
        return self.data['sounds']

    def __repr__(self):
        return "Definitions for: {}".format(self.keyword)

class Random:
    """Wrapper for urbandictionary's random words api
    """
    def __init__(self):
        r = requests.get(UD_RANDOM_URL)
        self.data, self.status_code = r.json(), r.status_code

    def get_random(self):
        """Returns a list object having 10 different definition

        :return: :class:`list`
        """
        return self.data['list']

    def __repr__(self):
        return "Random definitions class"


if __name__ == '__main__':
    m = Word('acid')
    print(m.get_tags())
    m = Random()
    print(m.get_random())
    m = Word()
