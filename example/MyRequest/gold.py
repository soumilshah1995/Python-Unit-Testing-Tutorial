import  requests


class Gold(object):
    def __init__(self):
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive'}
        self.url = " https://data-asg.goldprice.org/dbXRates/USD"

    @property
    def get(self):
        try:
            r = requests.get(url=self.url, headers= self.headers, timeout=1)
            if r.ok:
                return r
            else:
                return None
        except requests.exceptions.Timeout:
            return 'Bad Response'

#obj1 = Gold()
#print(obj1.get)
