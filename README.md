# 📊 Trading RSI + EMA Bot

🚀 Bot de trading automatizado que utiliza RSI + EMA con datos de Binance y genera señales en CSV.

![Banner](./banner.png)

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![MIT License](https://img.shields.io/badge/license-MIT-green)
![Binance](https://img.shields.io/badge/exchange-Binance-yellow)

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Paquetes necesarios:
  - `binance`
  - `pandas`
  - `pandas_ta`
  - `pyyaml`
  - `python-dotenv`

---

## 🛠️ Configuración

1. 🧪 Crear un archivo `.env` con tus claves de Binance Testnet:
```bash
API_KEY=tu_api_key
API_SECRET=tu_api_secret
```

2. ✏️ Editar `model_config.yaml` con tus parámetros preferidos:
```yaml
symbol: BTCUSDT
interval: 1h
strategy:
  ema_period: 21
  rsi_period: 14
  rsi_buy: 30
  rsi_sell: 70
```

---

## 🧪 Ejecución

```bash
cd src
python main.py
```

📁 El archivo `signals.csv` contendrá las señales generadas: BUY, SELL o HOLD.

---

## 📦 Estructura del Proyecto
```
📁 trading-rsi-ema-bot
├── src
│   ├── main.py              # Script principal
│   ├── strategy.py          # Estrategia RSI + EMA
│   └── data_handler.py      # Descarga de datos desde Binance
├── model_config.yaml        # Configuración de parámetros
├── .gitignore               # Archivos a excluir en Git
├── requirements.txt         # Dependencias
├── LICENSE                  # Licencia MIT
└── README.md                # Este archivo ✨
```

---

## 🌐 Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. ¡Libre de usar, mejorar y compartir! 💚

---

## 👨‍💻 Sobre el autor

Este proyecto fue creado por [Javier Morrón](https://github.com/javiermorron) — *IA, automatización y propósito: ese es mi lenguaje.*

🔗 Explorá más en: [https://javiermorron.com](https://javiermorron.com)