import numpy as np
import scipy.stats
import pandas as pd


def get_returns(rets: pd.DataFrame) -> pd.DataFrame:
    return rets.pct_change().dropna()


def compound_returns(rets: pd.DataFrame) -> pd.DataFrame:
    return np.expm1(np.log1p(rets).sum()) + 1


def annualize_rets(rets: pd.DataFrame, periods_per_year: int) -> pd.DataFrame:
    compounded_growth = compound_returns(rets)
    n_periods = rets.shape[0]
    return compounded_growth ** (periods_per_year / n_periods)


def skewness(rets: pd.DataFrame) -> pd.DataFrame:
    return scipy.stats.skew(rets)[0]


def kurtosis(rets: pd.DataFrame) -> pd.DataFrame:
    return scipy.stats.kurtosis(rets)[0]
