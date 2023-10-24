import os
import toolkit_config as cfg
from yf_example2 import yf_prc_to_csv


def qan_prc_to_csv(year):

    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    ticker = "QAN.AX"

    filename = f"qan_prc_{year}.csv"
    filepath = os.path.join(cfg.DATADIR, filename)

    print(start_date,end_date)
    yf_prc_to_csv(ticker, start_date, end_date, filepath)


if __name__ == "__main__":

    qan_prc_to_csv(2020)
