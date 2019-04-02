import pandas as pd


def get_proxy():
    df = pd.read_csv('proxy.txt')
    return df['ip'].values
