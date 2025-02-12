
# Integración con APIs externas (Alpha Vantage, etc.)

# api_integration.py
import requests

# Reemplaza con tu clave API de Alpha Vantage
ALPHA_VANTAGE_API_KEY = "YSOBJBRFVJLXY69E"

# Función para obtener el precio de la acción desde Alpha Vantage
def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",  # Puedes cambiar el intervalo a '1min', '15min', etc.
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        try:
            # Obtén el último precio de la acción
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            last_price = data["Time Series (5min)"][last_refreshed]["4. close"]
            return float(last_price)
        except KeyError:
            return "No se pudo obtener el precio."
    else:
        return "Error en la consulta de la API."

