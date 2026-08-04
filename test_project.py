import pandas

from project import get_returns, calculate_var, calculate_es


def test_get_returns():
    rendimientos = get_returns("AAPL")
    assert isinstance(rendimientos, pandas.Series)
    assert not rendimientos.empty
    assert not rendimientos.isna().any()


def test_calculate_var():
    rendimientos = pandas.Series([0.01, 0.02, -0.03, -0.05, 0.04, -0.01, 0.02, -0.04, 0.03, -0.02])
    assert calculate_var(rendimientos, 95) == rendimientos.quantile(0.05, interpolation="linear")
    assert calculate_var(rendimientos, 99) == rendimientos.quantile(0.01, interpolation="linear")


def test_calculate_es():
    rendimientos = pandas.Series([0.01, 0.02, -0.03, -0.05, 0.04, -0.01, 0.02, -0.04, 0.03, -0.02])
    var_his = calculate_var(rendimientos, 95)
    es_var = calculate_es(rendimientos, var_his)
    assert isinstance(es_var, float)
    assert es_var <= var_his
