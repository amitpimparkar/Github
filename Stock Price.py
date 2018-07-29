#Simple Program to ask for a Stock Symbol and display the price.

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()

code=input('Enter Code')

df = web.DataReader({code}, 'morningstar', start, end)

print(df.head(2))#df.Open/df.Close