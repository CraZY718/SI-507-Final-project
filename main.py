import pandas as pd
import networkx as nx
from preprocess import clean_data
from factor_generator import generate_factors
from network_builder import build_graph, export_graph_json
from cli_interface import launch_cli

# Load your data
data = pd.read_csv("data_2019-2024.csv")
data = clean_data(data)

# Group by ticker and compute factors for each stock
all_graphs = []
for ticker, group in data.groupby("TICKER"):
    try:
        factors_df = generate_factors(group)
        G = build_graph(factors_df, stock_ticker=ticker)
        all_graphs.append(G)
    except Exception as e:
        print(f"[WARN] Skipping {ticker}: {e}")

# Combine all individual graphs into one market graph
market_graph = nx.compose_all(all_graphs)
export_graph_json(market_graph, path="factor_network.json")

# Start CLI interface
launch_cli(market_graph)