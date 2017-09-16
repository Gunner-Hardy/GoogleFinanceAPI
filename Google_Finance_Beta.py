"""
GeneralCode.py
A program designed to work with Google Finance to provide basic stock evaluation data
@Author Gunner L Hardy
@version 2017-05-24
"""
import requests
import urllib.request, urllib.parse, urllib.error
import urllib.parse
import urllib
from lxml import html
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class GoogleAPI:
    """
    GoogleAPI Class defines a data set in terms of the data uses below
    """
    # 1 d = 86400
    linkage = {
        "quote": "https://www.google.com/finance/getprices?i=1&p=1m&f=c&df=cpct&q=",
        "data_quote": "https://www.google.com/finance/getprices?",
        "yearly_quote":"https://finance.google.com/finance/getprices?f=c&ei=Ef6XUYDfCqSTiAKEMg&q=",

    }

    def __init__(self):
        self.session = requests.session()
        self.session.proxies = urllib.request.getproxies()
    #Getting Data

    #Tests if Stock symbol is valid
    def stockTester(self, stock = None):
        if stock is None:
            stock = input("Symbol: ")
        # Check symbol
        try:
            pageContent = requests.get('https://www.google.com/finance?q=' + stock)
            tree = html.fromstring(pageContent.content)
            stockQuote = tree.xpath("//*[@id=\"price-panel\"]/div[1]/span[1]//text()")
            if stockQuote:
                return True
            else:
                raise NameError("Invalid Symbol: " + stock)
        except (ValueError):
            raise NameError("Invalid Symbol: " + stock)

    #Gets Current Quote
    def get_Current_Quote(self, stock=None): #Gets Current Price
        if self.stockTester(stock) == True:
            pageContent = requests.get('https://www.google.com/finance?q='+stock)
            tree = html.fromstring(pageContent.content)
            stockQuote = tree.xpath("//*[@id=\"price-panel\"]/div[1]/span[1]//text()")
            stockQuote2 = float(stockQuote[1])
            return (stockQuote2)
        else:
            print(self.stockTester(stock))



    #returns yearly close
    def get_Yearly_Price_Data(self, stock = None,period_in_years = None):
        data = self.stockTester(stock)
        urrl = str(self.linkage['yearly_quote'])+str(stock)+"&p="+str(period_in_years)+"Y"
        data = requests.get(urrl)
        txt = data.text
        loc_data = txt.find("DATA=")
        pricing_data = txt[loc_data:loc_data+10000000000]
        parsed_pricing_data = pricing_data.splitlines()
        parsed_pricing_data = list(filter(None,parsed_pricing_data))
        prefix = ('TIMEZONE','DATA')
        for word in parsed_pricing_data[:]:
            if word.startswith(prefix):
                parsed_pricing_data.remove(word)
        parsed_pricing_data = [float(i) for i in parsed_pricing_data]
        return parsed_pricing_data


