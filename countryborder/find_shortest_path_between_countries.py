import networkx as nx


def find_shortest_path_between_countries(G, source_country, target_country):  # noqa
    """
    Find and print the shortest path between two countries in the network.
    Parameters:
    G (networkx.Graph): The network of neighboring countries.
    source_country (str): The name of the source country.
    target_country (str): The name of the target country.
    This function finds the shortest path from the source country to the target country in the network,
    prints the minimum number of borders to cross, and displays the countries to traverse.
    """
    shortest_path = nx.shortest_path(G, source=source_country, target=target_country)

    # Print the minimum number of borders and the country names you have to cross
    print("Minimum number of borders to go from", source_country, "to", target_country, ":", len(shortest_path) - 1)
    print("Countries to cross:")
    for i in range(len(shortest_path) - 1):
        source = shortest_path[i]
        target = shortest_path[i + 1]
        print(f"{source} -> {target}")
