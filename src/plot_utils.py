import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Plot a subset of simulated price paths
def plot_sample_paths(paths: np.ndarray, n_paths_to_plot: int = 20):

    n_paths_to_plot = min(n_paths_to_plot, paths.shape[1])

    plt.figure(figsize=(10, 6))
    for i in range(n_paths_to_plot):
        plt.plot(paths[:, i], alpha=0.7)
    plt.title(f"Sample of {n_paths_to_plot} Simulated Price Paths")
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()

#Plot the distribution of final prices across simulations
def plot_final_price_distribution(paths: np.ndarray):
    
    final_prices = paths[-1, :]

    plt.figure(figsize=(8, 5))
    sns.histplot(final_prices, bins=50, kde=True)
    plt.title("Distribution of Final Simulated Prices")
    plt.xlabel("Final Price")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
