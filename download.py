import time
import pandas as pd
from pkg.symbols import grab_SP500_from_github_mfs_dataset as tickers
from pkg.yahoo import yahoo_minute_prices as minute_prices

def main():
    print(f'Ready to go...')
    tickers_list = tickers().Yahoo.to_list()
    print(f'tickers: {tickers_list}')
    start_time = time.time()
    
    prices_df = minute_prices(tickers_list)
    end_time = time.time()
    print(prices_df.loc[prices_df.Symbol == tickers_list[len(tickers_list)-1]])

    elapsed_time = end_time - start_time
    print(f'Execution time: {elapsed_time}')


if __name__ == '__main__':
    main()
