from pkg.trading import yahoo

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

