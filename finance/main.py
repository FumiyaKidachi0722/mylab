import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


def get_stock_chart(ticker_symbol, start_date, end_date):
    # ヤフーファイナンスから株価データを取得
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # データフレームから終値を取得
    close_prices = stock_data['Close']

    # データをプロット
    plt.figure(figsize=(14, 7))
    plt.plot(close_prices)
    plt.title('Stock Price Chart: ' + ticker_symbol)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid()
    plt.show()


# 使用例
get_stock_chart('AAPL', '2023-01-01', '2023-07-01')
