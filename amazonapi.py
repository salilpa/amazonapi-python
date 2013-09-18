from bs4 import BeautifulSoup
import requests
import re
class AMAZONAPI:

    url_amazon = "http://www.amazon.in/gp/product/"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"}
    error = ""

    def __init__(self,isbn10=""):
        self.response_json = {}
        if len(isbn10)!=10:
            raise ValueError(u'%s is not a valid isbn10 number as it does not have 10 digits' % isbn10)
        r = sum((10 - i) * (int(x) if x != 'X' else 10) for i, x in enumerate(isbn10))
        if r % 11 != 0:
            raise ValueError(u'%s is not valid isbn10 number' % isbn10)
        else:
            self.isbn10 = isbn10

    def request(self):
        r = requests.get(AMAZONAPI.url_amazon + self.isbn10,headers=AMAZONAPI.headers)
        if r.url == 'http://www.amazon.in/gp/homepage.html':
            self.error = "No record of book exists"
            return False
        else:
            soup = BeautifulSoup(r.text)
            self.__getDetails(soup)
            return True

    def __getDetails(self,soup):
        #set pnr
        self.response_json["isbn10"] = self.isbn10

    def get_json(self):
        return self.response_json

