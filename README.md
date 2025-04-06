# StockFactorNet Tool

---

## Project Overview

**StockFactorNet Tool** evaluates stock return behavior based on 9 key financial factors, they include **Momentum**, **Volatility**, **Liquidity**, **Amplitude**, **Dividend Yield** , **Gap return**, **Trading activity**,**Market correlation** and **Target return as dependent variable**.The project constructs a directed graph where factors are linked to stocks based on the statistical significance of their predictive power (via linear regression). This enables users to query and interpret stock-factor relationships interactively via a command-line interface (CLI).

---

## Features

1. **Analyze Factor Similarity Between Stocks**  
   Find stocks that have similar factor exposures based on shared incoming edges in the graph.

2. **Explore Influence Paths**  
   Use shortest-path analysis to explore how specific factors influence a given stock.

3. **Identify Key Drivers**  
   - **Most Influential Factor**: The factor affecting the most number of stocks.  
   - **Most Affected Stock**: The stock that is influenced by the highest number of factors.

4. **Inspect Nodes**  
   View metadata of any stock or factor node, including degree information.

5. **Export Network**  
   Automatically saves a `.json` version of the factor-stock graph using NetworkX format.

---

## How to Use

### Prerequisites

- Python 3.11 or above
- Dependencies:
  - `pandas`
  - `numpy`
  - `networkx`
  - `statsmodels`

You can install them via:

```bash
pip install pandas networkx statsmodels
```

---

## Running the Program

1. **Clone this repository**

```bash
git clone https://github.com/CraZY718/SI-507-Final-project.git
```

2. **Navigate to the project folder**

```bash
cd SI-507-Final-project
```

3. **Run the program**

```bash
python3 main.py
```

---

## Example CLI Interaction

```
Welcome to the Stock-Factor Network CLI!

Options:
1. Find similar stocks
2. Find shortest path
3. Show most influential factor
4. Show most affected stock
5. Get node info
6. Exit
```

### Example

- Select **Option 1**, enter `TSLA`  
  → Returns 5 stocks with the most similar factor profiles to TSLA.

- Select **Option 2**, enter `momentum → TSLA`  
  → Returns the path: `[momentum, TSLA]` if a connection exists.

---

## Required Python Packages

- `pandas`
- `numpy`
- `networkx`
- `statsmodels`

Install via:

```bash
pip install pandas numpy networkx statsmodels
```

---

## Repository Structure

```
.
├── main.py
├── cli_interface.py
├── preprocess.py
├── factor_generator.py
├── network_builder.py
├── data_2019-2024.csv
├── output/
│   └── factor_network.json
└── README.md
```

---

## Author

Developed by **Zongyuan Chen** for the SI 507 Final Project (Winter 2025).

