import yfinance as yf
import pandas

# prueba 
datos = yf.download("AAPL", period="2y")
precios = datos["Close"]
ticker = precios["AAPL"]
print(type(ticker))
rendimientos = ticker.pct_change()
print(rendimientos)



# funcion para extraer los retornos de las compañias en el periodo de dos años

def get_returns(ticker):
    datos = yf.download(ticker, period="2y")

## Var Historico
# obtener rendimientos diarios de cada compañia en los ultimos dos años
# ordenar rendiminetos de peor a mejor (pandas)
# eleccion nivel de confianza (95/99)


## VaR Expected Shortfall
# sacar la media de los rendimientos mas alla del VaR



