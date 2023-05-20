import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
day_before_yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
stock_response.raise_for_status()
stock_data = stock_response.json()
# print(stock_data["Time Series (Daily)"])
TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
y_closing_stock_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
# print(y_stock_price)
TODO 2. - Get the day before yesterday's closing stock price
dby_closing_stock_price = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
# print(dby_closing_stock_price)
TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff_closing_stock_price = (y_closing_stock_price - dby_closing_stock_price)
up_down = None
if diff_closing_stock_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_change = round((diff_closing_stock_price/y_closing_stock_price)*100)
# print(percent_change)
TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percent_change) > 1:
    # print("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_article = news_data["articles"]

TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = news_article[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent_change}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


Optional TODO: Format the message like this:
    for article in formatted_articles:
        message = client.messages.create(body=article, from_='+11234567890', to='+11234567890')
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

