import yfinance as yf
import pandas
import sys
import logging
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

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

    # Expected Shortfall
    es_var = calculate_es(datos,var_his)

    # grafica de VaR hitorico + Expected Shortfall
    plt.rcParams["font.family"] = "serif"

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(datos, bins=112, color="#0B2545", edgecolor="white", alpha=0.9)
    ax.axvline(var_his, color="#8B1E3F", linestyle="--", linewidth=2, label=f"VaR {confianza}%: {var_his*100:.2f}%")
    ax.axvline(es_var, color="#B08D2B", linestyle="--", linewidth=2, label=f"Expected Shortfall: {es_var*100:.2f}%")

    ax.set_title(f"Distribution of Returns — {ticker} ({confianza}% Confidence)", fontsize=14, pad=15)
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")
    ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.25)

    ax.legend(frameon=True, loc="upper right", fontsize=10)

    plt.savefig(f"VaR_his_{ticker}_{confianza}.png", dpi=300, bbox_inches="tight")
    plt.show()

    

# funcion para extraer los retornos de las compañias en el periodo de dos años
def get_returns(ticker):
    datos = yf.download(ticker, period="2y", progress=False)    # sacar los rendimientos diarios de cada compañia en los ultimos dos años

    col_close = datos["Close"]
    serie_ticker = col_close[ticker]
    rendimientos = serie_ticker.pct_change().dropna()   # sacar rendimientos diarios, eliminar datos Na
    return rendimientos

# funcion para el VaR historico
def calculate_var(rendimientos, confianza):
    q = 1 - (confianza/100)
    var_his = rendimientos.quantile(q, interpolation='linear')
    return var_his

# funcion para el Expected Shortfall
def calculate_es(rendimientos, var_his):
    es_var = rendimientos[rendimientos < var_his]
    es_var = es_var.mean()
    return es_var



if __name__ == "__main__":
    main()
