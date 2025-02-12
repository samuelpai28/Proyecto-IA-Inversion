# Lógica de inversiones (cálculos, estrategias)

import requests

def calculate_roi(investment, profit):
    """Calcula el retorno sobre inversión (ROI)."""
    return (profit - investment) / investment * 100

def get_stock_price(symbol):
    """Obtiene el precio de una acción (puedes integrarlo con una API de finanzas)."""
    # Aquí iría el código para consultar una API, por ejemplo, Alpha Vantage o Yahoo Finance
    return 100  # Valor ficticio para prueba

def calculate_compound_growth(principal, rate, years):
    """Calcula el crecimiento compuesto."""
    return principal * (1 + rate) ** years