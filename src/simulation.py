import numpy as np


#Runs the Monte Carlo simulation using the GBM formula
def simulate_gbm_paths(
    S0: float,
    mu: float,
    sigma: float,
    n_days: int,
    n_sims: int,
    random_seed: int | None = None
) -> np.ndarray:
    """
    Simulate GBM price paths.
    Returns array of shape (n_days + 1, n_sims).
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    dt = 1.0  # daily steps
    paths = np.zeros((n_days + 1, n_sims))
    paths[0] = S0

    Z = np.random.normal(size=(n_days, n_sims))

    for t in range(1, n_days + 1):
        paths[t] = paths[t - 1] * np.exp(
            (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[t - 1]
        )

    return paths
