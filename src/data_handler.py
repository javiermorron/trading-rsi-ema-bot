from binance.client import Client
import pandas as pd
import os

client = Client(os.getenv("API_KEY"), os.getenv("API_SECRET"))

def get_historical_data(symbol, interval):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=500)
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume", "close_time",
        "quote_asset_volume", "trades", "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    df["close"] = pd.to_numeric(df["close"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df[["timestamp", "close"]]
