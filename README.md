# Monte Carlo Stock Price Simulator (GBM)

This project implements a full Monte Carlo simulation of stock prices using the Geometric Brownian Motion (GBM) model. It loads real historical market data, estimates drift and volatility from log returns, simulates thousands of future price paths, and visualizes the results. A demonstration file is included in the structure

## Project Structure

```
monte-carlo-stock-sim/
├── data/
├── src/
│   ├── data_loader.py
│   ├── gbm.py
│   ├── simulation.py
│   └── plot_utils.py
├── notebooks/
│   └── stock_monte_carlo.ipynb
├── stock_monte_carlo_demo.ipynb
├── README.md
└── requirements.txt
```

## Features

- Download historical stock data using `yfinance`
- Compute daily log returns
- Estimate GBM drift and volatility parameters
- Simulate thousands of Monte Carlo price paths
- Visualize sample paths and final price distribution
- Compute risk metrics (percentiles, downside probability, VaR)

## How to Run

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
   
2. Open the notebook:

   ```
   jupyter notebook notebooks/stock_monte_carlo.ipynb
   ```
   
3. Run all cells to reproduce the analysis.

## Requirements

See `requirements.txt` for the full dependency list.

## License

This project is for educational and research purposes.
