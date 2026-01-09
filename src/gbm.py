import numpy as np
import pandas as pd

#Estimate daily and annualized GBM parameters from log returns
def estimate_gbm_params(log_returns: pd.Series, trading_days: int = 252):
    mu_daily = log_returns.mean()
    sigma_daily = log_returns.std()

    mu_annual = mu_daily * trading_days
    sigma_annual = sigma_daily * np.sqrt(trading_days)

    return {
        "mu_daily": mu_daily,
        "sigma_daily": sigma_daily,
        "mu_annual": mu_annual,
        "sigma_annual": sigma_annual,
    }
