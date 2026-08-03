import yfinance as yf
import pandas




def main():
    # input de ticker
    try:
        ticker = input("Enter the stock ticker you want to analyze: ").upper()
        if ticker is (lista o diccionario de tikes validos que tengo que hacer):
            pass
        else:
            raise ValueError
    except ValueError:
        print("Invalid ticker")

    # input de confianza
    try:
        confianza = int(input("Choose confidence level, 95 or 99: "))
        if confianza == 95 or confianza == 99:
            pass
        else:
            raise ValueError
    except ValueError:
        print("99 or 95")
    

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


def calculate_var(rendimientos, confianza):

    q = 1 - (confianza/100)
    var_his = rendimientos.quantile(q, interpolation='linear')
    return var_his



def calculate_es():
    pass
    

