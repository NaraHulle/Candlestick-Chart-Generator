# Candlestick Chart Generator

A python tool to generate candlestick charts for visualizing cryptocurrency price movements.

__1. Data Retrieval:__

 - The ```fetch_historical_data``` method fetches historical price data from the specified API using the ```requests``` library and stores it in the ```self.data``` variable.
   
__2. Chart Generation:__

 - The ```generate_candlestick_chart``` method converts the data to a pandas DataFrame for analysis.
 - The DataFrame is processed to convert the 'date' column to a datetime format and set it as the index.
 - A candlestick chart is generated using ```mplfinance``` with the specified chart style, title, labels, and additional settings such as non-trading day display, figure ratio, figure scale, moving averages, and volume display.

__3. Usage:__

 - Make sure you have the required libraries ```requests```, ```pandas```, ```mplfinance``` installed before running the code. You can install them using the following commands:
   ```bash
   pip install requests
   pip install pandas
   pip install mplfinance
   ```
 - To use this code, replace the ```api_url``` variable with the actual API endpoint to fetch historical price data for your desired cryptocurrency and trading pair. Additionally, customize the chart appearance and indicators by modifying the parameters of the ```mpf.plot``` function in the ```generate_candlestick_chart``` method.

   -----
   
   
