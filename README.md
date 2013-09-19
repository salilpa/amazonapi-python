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
            'book details': u'About the Book Five thousand years ago, there came to earth a magical being called Krishna, who brought about innumerable miracles for the good of mankind. Humanity despaired of its fate if the Blue God were to die but was reassured that he would return in a fresh avatar when needed in the eventual Dark Age - the Kaliyug. In modern times, a poor little rich boy grows up believing that he is that final avatar. Only, he is a serial killer. In this heart stopping tale, the arrival of a murderer who executes his gruesome and brilliantly thought-out schemes in the name of God is the first clue to a sinister conspiracy to expose an ancient secret - Krishna\u2019s priceless legacy to mankind. Historian Ravi Mohan Saini must breathlessly dash from the submerged remains of Dwarka and the mysterious lingam of Somnath to the icy heights of Mount Kailash, in a quest to discover the cryptic location of Krishna\u2019s most prized possession. From the sand washed ruins of Kalibangan to a Vrindavan temple destroyed by Aurangzeb, Saini must also delve into antiquity to prevent a gross miscarriage of justice. Ashwin Sanghi, bestselling author of \u2018The Rozabal Line\u2019 and \u2018Chanakya\u2019s Chant\u2019, brings you yet another exhaustively researched whopper of a plot, while providing an incredible alternative interpretation of the Vedic Age that will be relished by conspiracy buffs and thriller addicts alike.'
        },
    'isbn10': '9381626685',
    'list price': u'Rs. 250.00',
    'product description':
        {
            u'About the Author': u"Ashwin Sanghi entrepreneur by day, novelist by night has all the usual qualifications of an Indian businessman. Schooling at the Cathedral and John Connon School, a B.A. (Economics) from St. Xavier's College and an M.B.A. (Finance) from the Yale School of Management. Ashwin is a director of the M.K. Sanghi Group of Companies, which has business interests in real estate development, automobiles, manufacturing and engineering. Besides being a businessman, Ashwin manages a parallel career as writer of fiction. Ashwin's first novel, The Rozabal Line was originally self-published in 2007 under his anagram-pseudonym Shawn Haigins. The book was subsequently published by Westland in 2008 and 2010 in India under his own name and went on to become a national bestseller. Chanakya s Chant is his second novel in the historical fiction genre. The book has remained on AC Nielsen's India Bookscan Top-10 for all of 2011. It won the 2010 Crossword-Vodafone Popular Choice Award in September 2011. UTV has purchased the movie rights to the book and a film based upon the story is expected soon. Dr. Shashi Tharoor released the novel in Mumbai calling it an enthralling, delightfully interesting and gripping read with historical research that is impressive. The Hindustan Times has called it a cracker of a page-turner. Ashwin is also working towards a Ph.D. in Creative Writing from Bangor University in Wales. Ashwin lives in Mumbai with his wife, Anushika and his eight-year old son, Raghuvir."
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

