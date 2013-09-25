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

Sample Request through Command Line
--------------
    python main.py 9382618341 9381626685

Sample Response
---------------
The reponse is a json object as follows:

    {
        'product details': {
            'Publisher': 'Westland (27 February 2013)',
            'Paperback': '600 pages',
            'Average Customer Review': '4.2 out of 5 stars',
            'Language': 'English',
            'Product Dimensions': '19.6 x 12.8 x 3.8 cm',
            'Amazon Bestsellers': {
                'in Books > Literature & Fiction > Myths, Legends & Sagas': '1',
                'Books': '1',
                'in Books > Literature & Fiction > Indian Writing': '1'
            },
            'ISBN-10': '9382618341',
            'ISBN-13': '978-9382618348'
        },
        'book description': {
            'Series': 'Shiva Trilogy (Book 3)',
            'Publication Date': '27 February 2013',
            'book details': "About The BookEVIL HAS RISEN.ONLY A GOD CAN STOP IT.Shiva is gathering his forces. He reaches the Naga capital, Panchavati, and Evil is finally revealed. The Neelkanth prepares for a holy war against his true enemy, a man whose name instils dread in the fiercest of warriors.India convulses under the onslaught of a series of brutal battles. It's a war for the very soul of the nation. Many will die. But Shiva must not fail, no matter what the cost. In his desperation, he reaches out to the ones who have never offered any help to him the Vayuputras.Will he succeed? And what will be the real cost of battling Evil? To india? And to Shiva's soul?Discover the answer to these mysteries in this concluding part of the bestselling Shiva Trilogy."
        },
        'isbn10': '9382618341',
        'title': 'The Oath of the Vayuputras (Shiva Trilogy) [Paperback]',
        'product description': {
            'About the Author': 'Amish is a 1974-born, IIM (Kolkata)-educated, boring banker turned happy author. The success of his debut book, The Immortals of Meluha (Book 1 of the Shiva Trilogy), encouraged him to give up a fourteen-yearold career in financial services to focus on writing. He is passionate about history, mythology and philosophy, finding beauty and meaning in all world religions.'
        },
        'list price': 'Rs. 350.00',
        'actual price': 'Rs. 175.00'
    }

[1]: http://www.crummy.com/software/BeautifulSoup/
[2]: https://github.com/kennethreitz/requests

