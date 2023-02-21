from pkg import yahoo

def test_yahoo_prices():
    tickers = ['TSLA', 'AAPL']
    current_day = '2023-01-31'
    prices_df = yahoo.yahoo_prices(tickers, current_day)
    assert prices_df is not None
    assert len(prices_df.Symbol.unique()) == len(tickers)

def test_yahoo_prices_without_list():
    ticker = 'TSLA'
    current_day = '2023-01-31'
    prices_df = yahoo.yahoo_prices(ticker, current_day)
    assert prices_df is None

def test_yahoo_prices_with_list_of_one():
    tickers = ['TSLA']
    current_day = '2023-01-31'
    prices_df = yahoo.yahoo_prices(tickers, current_day)
    assert prices_df is None

def test_yahoo_minute_prices():
    tickers = ['TSLA', 'AAPL']
    prices_df = yahoo.yahoo_minute_prices(tickers)
    print(prices_df.loc[prices_df.Symbol == 'TSLA'].tail(10))
    assert prices_df is not None