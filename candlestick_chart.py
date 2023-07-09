import requests
import pandas as pd
import mplfinance as mpf

class CandlestickChartGenerator:
    def __init__(self, api_url, symbol):
        self.api_url = api_url
        self.symbol = symbol
        self.data = None

    def fetch_historical_data(self):
        # Fetch historical price data from the API
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error fetching historical data from the API.")

    def generate_candlestick_chart(self):
        # Convert data to pandas DataFrame for analysis
        df = pd.DataFrame(self.data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        df['date'] = pd.to_datetime(df['date'], unit='s')
        df.set_index('date', inplace=True)

        # Generate candlestick chart using mplfinance
        mpf.plot(df, type='candle', style='yahoo', title=f'{self.symbol} Candlestick Chart',
                 ylabel='Price', ylabel_lower='Volume', show_nontrading=True,
                 figratio=(16, 9), figscale=1.5, mav=(20, 50), volume=True)

# Example usage:

# Define API URL and symbol
api_url = "https://api.example.com/historical-data"
symbol = "BTC/USD"

# Create an instance of CandlestickChartGenerator
chart_generator = CandlestickChartGenerator(api_url, symbol)

# Fetch historical price data
chart_generator.fetch_historical_data()

# Generate candlestick chart
chart_generator.generate_candlestick_chart()
