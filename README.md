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
  - `python-binance`
  - `pandas`
  - `pandas_ta`
  - `pyyaml`
  - `python-dotenv`
  - `numpy==1.23.1`
  - `setuptools==65.5.0`

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

## 🧯 Problemas comunes y soluciones

🔹 **Error:** `ModuleNotFoundError: No module named 'yaml'`
- 💡 Solución: Ejecutar `pip install pyyaml`

🔹 **Error:** `ModuleNotFoundError: No module named 'binance'`
- 💡 Solución: Ejecutar `pip install python-binance`

🔹 **Error:** `ImportError: cannot import name 'NaN' from 'numpy'`
- 💡 Solución 1: Ejecutar `pip install numpy==1.23.1`
- 💡 Solución 2 (alternativa definitiva): Editar el archivo `squeeze_pro.py` en `pandas_ta` y reemplazar:
  ```python
  from numpy import NaN as npNaN
  ```
  por:
  ```python
  import numpy as np
  npNaN = np.nan
  ```

🔹 **Error:** `pkgutil has no attribute 'ImpImporter'`
- 💡 Solución: Ejecutar `pip install setuptools==65.5.0`

🔹 **Error:** `ModuleNotFoundError: No module named 'pkg_resources'`
- 💡 Solución: Ejecutar `pip install setuptools`

🔹 **Recomendación:** usar un entorno virtual limpio:
```bash
python -m venv env
env\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## 🌐 Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. ¡Libre de usar, mejorar y compartir! 💚

---

## 👨‍💻 Sobre el autor

Este proyecto fue creado por [Javier Morrón](https://github.com/javiermorron) — *IA, automatización y propósito: ese es mi lenguaje.*

🔗 Explorá más en: [https://javiermorron.com](https://javiermorron.com)