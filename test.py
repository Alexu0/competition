import gdax
import pandas as pd
import os
#import plotly.plotly as py
#import plotly.graph_objs as go
public_client=gdax.PublicClient()
data=public_client.get_product_historic_rates('ETH-USD', granularity=300)
df=pd.DataFrame(data)
df.columns=['time','low','high','open','close','volume']

