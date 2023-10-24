# Downloads Qantas share price beginning 14 September 2022
import yfinance
tic = "QAN.AX"
start = '2022-09-14'
end = None
df = yfinance.download(tic, start, end, ignore_tz=True)
print(df)
df.to_csv('qan_stk_prc.csv')

import yfinance

start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

tic = "QAN.AX"

# Convert the ticker to lower case
tic_base = tic.lower()              # --> 'qan.ax'
print(tic_base)

# Split the string into a list,
# using '.' as a separator
tic_base = tic_base.split('.')    # --> ['qan', 'ax']
print(tic_base)
# Fetch the first element of the list
tic_base = tic_base[0]


