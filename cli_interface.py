import networkx as nx

def get_similar_stocks(graph, ticker):
    target_factors = set(pred for pred in graph.predecessors(ticker))
    similar = []
    for node in graph.nodes:
        if graph.nodes[node].get('type') == 'stock' and node != ticker:
            other_factors = set(pred for pred in graph.predecessors(node))
            jaccard = len(target_factors & other_factors) / len(target_factors | other_factors | {1e-5})
            similar.append((node, jaccard))
    similar.sort(key=lambda x: x[1], reverse=True)
    return similar[:5]

def shortest_path(graph, source, target):
    try:
        return nx.shortest_path(graph, source=source, target=target)
    except nx.NetworkXNoPath:
        return f"No path found from {source} to {target}."

def most_influential_factor(graph):
    factors = [n for n, attr in graph.nodes(data=True) if attr.get('type') == 'factor']
    return max(factors, key=lambda f: graph.out_degree(f))

def most_affected_stock(graph):
    stocks = [n for n, attr in graph.nodes(data=True) if attr.get('type') == 'stock']
    return max(stocks, key=lambda s: graph.in_degree(s))

def get_node_info(graph, node):
    if node not in graph:
        return f"Node {node} not found."
    info = {
        'type': graph.nodes[node].get('type'),
        'in_degree': graph.in_degree(node),
        'out_degree': graph.out_degree(node)
    }
    return info

def launch_cli(graph):
    print("\nWelcome to the Stock-Factor Network CLI!")
    while True:
        print("\nOptions:")
        print("1. Find similar stocks")
        print("2. Find shortest path")
        print("3. Show most influential factor")
        print("4. Show most affected stock")
        print("5. Get node info")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            ticker = input("Enter stock ticker [e.g. TSLA]: ")
            print(get_similar_stocks(graph, ticker))
        elif choice == '2':
            source = input("Enter source node (Factor [momentum/volatility/liquidity/amplitude/dividend_yield/gap_return/trading_activity/market_corr/target_return]): ")
            target = input("Enter target node (Stock name [e.g. TSLA]): ")
            print(shortest_path(graph, source, target))
        elif choice == '3':
            print("Most influential factor:", most_influential_factor(graph))
        elif choice == '4':
            print("Most affected stock:", most_affected_stock(graph))
        elif choice == '5':
            node = input("Enter node name (factor or stock): ")
            print(get_node_info(graph, node))
        elif choice == '6':
            print("Exiting CLI.")
            break
        else:
            print("Invalid choice. Try again.")
