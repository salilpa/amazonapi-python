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
        'isbn10': '9381626685'
	}

[1]: http://www.crummy.com/software/BeautifulSoup/
[2]: https://github.com/kennethreitz/requests

