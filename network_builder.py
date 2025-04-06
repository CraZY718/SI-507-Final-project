
import networkx as nx
import statsmodels.api as sm
import pandas as pd
import json
from networkx.readwrite import json_graph

def build_graph(df, stock_ticker):
    # Build a directed graph based on regression of factors to target return
    G = nx.DiGraph()

    dependent_var = 'target_return'
    independent_vars = [col for col in df.columns if col not in ['date', dependent_var]]

    # Fit regression model
    X = sm.add_constant(df[independent_vars])
    y = df[dependent_var]
    model = sm.OLS(y, X).fit()

    # Add stock node
    G.add_node(stock_ticker, type='stock')

    for factor in independent_vars:
        coef = model.params.get(factor, 0)
        pval = model.pvalues.get(factor, 1)

        # Add factor node
        G.add_node(factor, type='factor')

        # Create edge if coefficient is significant
        if pval < 0.1:
            G.add_edge(factor, stock_ticker, weight=coef, p_value=pval)

    return G

def export_graph_json(graph, path):
    data = json_graph.node_link_data(graph)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
