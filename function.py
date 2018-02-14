import gdax
import pandas as pd
import os
def historical_data(pair='BTC-USD',resolution=300):
    public_client = gdax.PublicClient()
    data = public_client.get_product_historic_rates(pair, granularity=resolution)
    try:
        df = pd.DataFrame(data)
    except:
        print (data)
    df.columns = ['time', 'low', 'high', 'open', 'close', 'volume']
    _location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path = _location_ + "/data_csv/gdax_"+pair+".csv"
    directory = os.path.dirname(path)
    if os.path.exists(directory):
        df.to_csv(path)
    else:
        os.mkdir(directory)
        df.to_csv(path)
    return