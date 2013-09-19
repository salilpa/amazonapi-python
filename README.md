pnrapi-python
=============

A Python web-scraper for Amazon India book store.

Requirements
------------
* [Beautiful Soup 4][1]
  - `pip install beautifulsoup4` or `easy_install beautifulsoup4`
* [Requests][2]
  - `pip install requests` or `easy_install requests`

Sample Request
--------------
    import amazonapi
    p = amazonapi.AMAZONAPI("9381626685") #10-digit ISBN code
    if p.request() == True:
        print p.get_json()
    else:
        print p.error

Sample Response
---------------
The reponse is a json object as follows:

{
    'actual price': u'Rs. 145.00',
    'book description':
        {
            u'Publication Date': u'20 August 2012',
            'book details': u'About the Book Five thousand years ago'
        },
    'isbn10': '9381626685',
    'list price': u'Rs. 250.00',
    'product description':
        {
            u'About the Author': u"Ashwin Sanghi entrepreneur"
        },
    'product details':
        {
            'Amazon Bestsellers':
                {
                    u'in\xa0Books > Crime, Thriller & Mystery': u'7',
                    u'in\xa0Books > Literature & Fiction > Indian Writing': u'19'
                },
            u'Average Customer Review': u'4.1 out of 5 stars',
            u'ISBN-10': u'9381626685',
            u'ISBN-13': u'978-9381626689',
            u'Language': u'English',
            u'Paperback': u'485 pages',
            u'Product Dimensions': u'17 x 10.9 x 3.3 cm',
            u'Publisher': u'Westland Limited (20 August 2012)'
        },
    'title': u'The Krishna Key [Paperback]'
}

[1]: http://www.crummy.com/software/BeautifulSoup/
[2]: https://github.com/kennethreitz/requests

