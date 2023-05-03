import numpy as np
import scipy.stats


def get_returns(rets):
    return rets.pct_change().dropna()


def compound_returns(rets):
    return np.expm1(np.log1p(rets).sum()) + 1


def annualize_rets(rets, periods_per_year):
    compounded_growth = compound_returns(rets)
    n_periods = rets.shape[0]
    return compounded_growth ** (periods_per_year / n_periods)


def skewness(rets):
    return scipy.stats.skew(rets)[0]


def kurtosis(rets):
    return scipy.stats.kurtosis(rets)[0]
