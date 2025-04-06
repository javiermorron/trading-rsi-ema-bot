import pandas as pd
import pandas_ta as ta

def generate_signals(df, params):
    df.set_index("timestamp", inplace=True)
    df["ema"] = ta.ema(df["close"], length=params["ema_period"])
    df["rsi"] = ta.rsi(df["close"], length=params["rsi_period"])
    df["signal"] = "HOLD"
    df.loc[df["rsi"] < params["rsi_buy"], "signal"] = "BUY"
    df.loc[df["rsi"] > params["rsi_sell"], "signal"] = "SELL"
    return df.reset_index()
