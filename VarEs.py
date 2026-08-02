import yfinance as yf
import pandas


datos = yf.download("AAPL", period="2y")
precios = datos["Close"]
ticker = precios["AAPL"]
print(type(ticker))
rendimientos = ticker.pct_change()
print(rendimientos)



# funcion para extraer los retornos de las compañias en el periodo de dos años

def get_returns(ticker):
    datos = yf.download("AAPL", period="2y")
    



