import pandas as pd
import requests
import io
import requests


def grab_from_HTML_file():
    # Grab S&P Symbols from Wikipedia or local HTML File
    # wiki_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    # wiki_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks'
    tickers = pd.read_html("./tickers.html")[0]
    #tickers = tickers.Symbol.to_list()

    return tickers


def grab_SP500_from_wikipedia():
    # wiki_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks'
    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    s = requests.get(wiki_url).content
    tickers = pd.read_html(io.StringIO(s.decode("utf-8")))

    return tickers[0]


def grab_SP500_from_github_mfs_dataset():
    url = "https://raw.githubusercontent.com/MapleFrogStudio/DATASETS/main/STOCK_SYMBOLS/CSV/sp500.csv"
    tickers = pd.read_csv(url, header=0, index_col=None)

    return tickers
