import yfinance as yf
import pandas

## VaR Historico
# funcion para extraer los retornos de las compañias en el periodo de dos años

def get_returns(ticker):
    datos = yf.download(ticker, period="2y")    # sacar los rendimientos diarios de cada compañia en los ultimos dos años
    col_close = datos["Close"]
    serie_ticker = col_close[ticker]
    rendimientos = serie_ticker.pct_change().dropna() # sacar rendimientos diarios, eliminar datos Na
    return rendimientos

# eleccion nivel de confianza (95/99)


## VaR Expected Shortfall
# sacar la media de los rendimientos mas alla del VaR

print(get_returns("AAPL"))
    

