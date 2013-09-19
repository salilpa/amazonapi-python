from bs4 import BeautifulSoup
import requests
class AMAZONAPI:

    url_amazon = "http://www.amazon.in/gp/product/"#this will be the base url for all the product. ISBN10 number will be appended to this
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"}
    error = ""

    def __init__(self,isbn10=""):
        self.response_json = {}
        if len(isbn10)!=10: #len should be 10
            raise ValueError(u'%s is not a valid isbn10 number as it does not have 10 digits' % isbn10)
        r = sum((10 - i) * (int(x) if x != 'X' else 10) for i, x in enumerate(isbn10))
        if r % 11 != 0: #rule for a valid isbn10
            raise ValueError(u'%s is not valid isbn10 number' % isbn10)
        else:
            self.isbn10 = isbn10

    def request(self):
        r = requests.get(AMAZONAPI.url_amazon + self.isbn10,headers=AMAZONAPI.headers)
        if r.url == 'http://www.amazon.in/gp/homepage.html':
            self.error = "No record of book exists"
            return False
        else:
            soup = BeautifulSoup(r.text,'html.parser')#special parser as the default one fails
            self.__getDetails(soup)
            return True

    def __getDetails(self,soup):
        #set pnr
        self.response_json["isbn10"] = self.isbn10
        title = soup.find(id='btAsinTitle')
        list_price = soup.find(id='listPriceValue')
        actual_price = soup.find(id='actualPriceValue')
        book_description = soup.find(id='ps-content')
        product_description = soup.find(id='productDescription')
        product_details = soup.find('td', class_='bucket') #all isbn values and other data are stored here
        if title:
            self.response_json["title"] = title.text.strip()
        if list_price:
            self.response_json["list price"] = list_price.text.strip()
        if actual_price:
            self.response_json["actual price"] = actual_price.text.strip()
        if book_description:
            book_desc_json = {}
            span_content = book_description.find_all('span', attrs={'class':None})#this contains all the content
            span_heading = book_description.find_all('span', class_='byLinePipe')#this contains all the title
            for title, content in zip(span_heading, span_content):
                if title.text != '' and content.text != '':#assigning key values to each
                    book_desc_json[title.text.strip().replace(':','')] = content.text.strip()
            book_details = soup.find(id='postBodyPS')
            if book_details:
                book_desc_json['book details'] = book_details.text.strip()
            self.response_json["book description"] = book_desc_json

        if product_description:
            product_desc_json = {}
            product_desc_titles = product_description.find_all('h3', class_='productDescriptionSource')
            product_desc_contents = product_description.find_all('div', class_='productDescriptionWrapper')
            for title, content in zip(product_desc_titles, product_desc_contents):#iterating over both objects at once
                if title.text != '' and content.text != '':#assigning key values to each
                    product_desc_json[title.text.strip()] = content.text.strip()
            self.response_json["product description"] = product_desc_json

        if product_details:
            product_details = {}
            li_tags = soup.find_all('li', attrs={'class':None})
            for li in li_tags:
                title = li.find('b')
                if title:
                    if title.text.strip() == 'Average Customer Review:':
                        rating = li.find('span', class_ = 'swSprite')
                        if rating:
                            product_details[title.text.strip().replace(':','')] = rating.text.strip()
                    elif title.text.strip() == 'Amazon Bestsellers Rank:':
                        amazon_bestsellers = {}
                        ranks = li.find_all('li', class_='zg_hrsr_item')
                        for item in ranks:
                            category = item.find('span', class_='zg_hrsr_ladder')
                            rank = item.find('span', class_='zg_hrsr_rank')
                            if rank and category:
                                amazon_bestsellers[category.text.strip()] = rank.text.strip().replace('#','')
                        product_details['Amazon Bestsellers'] = amazon_bestsellers
                    else:
                        product_details[title.text.strip().replace(':','')] = li.text.replace(title.text,"").strip()
            self.response_json["product details"] = product_details

    def get_json(self):
        return self.response_json

