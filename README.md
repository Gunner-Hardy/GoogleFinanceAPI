# GoogleFinanceAPI
This is designed to pull data from Google Finance. 
# Current Features

    Pulling Daily Close Data (GoogleAPI.get_Yearly_Price_Data)
    Getting Current Quote (GoogleAPI.get_Current_Quote)
    
    More coming soon...

# Python 3
Project is designed for Python 3 Framwork

# How to Use (example)
#pulling AAPL's close price for the past 5 years

from GoogleAPI import GoogleAPI

google_data = GoogleAPI()

AAPL_data = google_data.get_Yearly_Price_Data(stock = 'AAPL', period_in_years = 5)

current_quote = google_data.get_Current_Quote('AAPL')

# More Features Coming Soon (also available on request)

This is not endorsed or affiliated with Google in any way.
