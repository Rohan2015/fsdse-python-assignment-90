import pandas as pd


def equal_operator(ds1, ds2):
    ds3 = (ds1 == ds2)
    return ds3
    #return pd.Series.tolist(ds3)

def greater_than_operator(ds1, ds2):
    ds3 = (ds1 > ds2)
    return ds3
    #return pd.Series.tolist(ds3)


def less_than_operator(ds1, ds2):
    ds3 = (ds1 < ds2)
    return ds3
    #return pd.Series.tolist(ds3)
