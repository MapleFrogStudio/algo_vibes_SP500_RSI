import pytest
from pkg import symbols, yahoo, strategy

@pytest.fixture
def raw_data():
    symbols_list = symbols.grab_SP500_from_github_mfs_dataset()
    symbols_list = symbols_list.Symbol.to_list()
    raw_prices = yahoo.yahoo_prices(symbols_list[2:5], '2023-01-31')
    
    return raw_prices

def test_setup_multi_asset(raw_data):
    tickers = raw_data.Symbol.unique().tolist()
    multi_asset = strategy.setup_multi_asset(raw_data)
    
    assert len(multi_asset) == len(tickers)
    for i in range(len(tickers)):
        assert multi_asset[i].Symbol[0] == tickers[i]
    
    #print(raw_data.Symbol.unique().tolist())
    #print(multi_asset[0].Symbol[0])
