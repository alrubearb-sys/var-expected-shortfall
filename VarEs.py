import yfinance as yf
import pandas
import sys
import logging
import matplotlib.pyplot as plt

logging.getLogger("yfinance").setLevel(logging.CRITICAL) # elimina el mensaje de error en el terminal si "Invalid Ticker"


def main():

    # input de ticker
    ticker = input("Enter the stock ticker you want to analyze: ").upper().strip()
    datos = get_returns(ticker)
    try:    # pruebo que el ticker tiene datos y es valido
        if datos.empty is True:
            raise ValueError
    except ValueError:
            sys.exit("Invalid ticker")

    # input de confianza
    try:
        confianza = int(input("Choose confidence level, 95 or 99: "))
        if confianza == 95 or confianza == 99:
            pass
        else:
            raise ValueError
    except ValueError:
        sys.exit("99 or 95")

    # VaR historico + hacer la grafica
    var_his = calculate_var(datos, confianza)

    plt.figure(figsize=(10,6))
    plt.hist(datos, bins=50, color="#184a79", edgecolor="white", alpha=0.85)
    plt.text(0.05, 0.05, f"VaR: {var_his*100:.2f}%", transform=plt.gca().transAxes, ha="left", va="bottom")
    plt.axvline(var_his, color="crimson", linestyle="--", linewidth=2)
    plt.title(f"Distribution of returns - {ticker} - {confianza}%")
    plt.xlabel("Daily return")
    plt.ylabel("Frequency")
    plt.grid(alpha=0.3)
    plt.savefig(f"VaR_his_{ticker}_{confianza}.png", dpi=300, bbox_inches="tight")
    plt.show()

# funcion para extraer los retornos de las compañias en el periodo de dos años
def get_returns(ticker):
    datos = yf.download(ticker, period="2y", progress=False)    # sacar los rendimientos diarios de cada compañia en los ultimos dos años

    col_close = datos["Close"]
    serie_ticker = col_close[ticker]
    rendimientos = serie_ticker.pct_change().dropna()   # sacar rendimientos diarios, eliminar datos Na
    return rendimientos


## VaR Expected Shortfall
# sacar la media de los rendimientos mas alla del VaR
def calculate_var(rendimientos, confianza):
    q = 1 - (confianza/100)
    var_his = rendimientos.quantile(q, interpolation='linear')
    return var_his


def calculate_es():
    pass


if __name__ == "__main__":
    main()
