import yaml
from data_handler import get_historical_data
from strategy import generate_signals

with open("../model_config.yaml", "r") as file:
    config = yaml.safe_load(file)

symbol = config["symbol"]
interval = config["interval"]
data = get_historical_data(symbol, interval)
signals = generate_signals(data, config["strategy"])
signals.to_csv("../signals.csv")
print("Señales generadas y guardadas en signals.csv")
