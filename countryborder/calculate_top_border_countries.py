
def calculate_top_border_countries(G, num_top_countries=10):  # noqa
    """
    Calculate the number of neighboring countries for each country node in the network.
    Parameters:
    G (networkx.Graph): The network of neighboring countries.
    num_top_countries (int): The number of top countries to display.
    This function calculates the number of neighboring countries for each country node,
    sorts the countries by the number of borders in descending order, and prints the top countries.
    """
    border_counts = {}
    border_countries = {}

    # Calculate the number of neighboring countries for each country node
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        border_counts[node] = len(neighbors)
        border_countries[node] = neighbors

    # Sort the countries by the number of borders (in descending order)
    top_countries = sorted(border_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the top countries with the most borders and their neighboring countries
    for i, (country, count) in enumerate(top_countries):
        if i < num_top_countries:
            neighbors = border_countries[country]
            print(f'{country} ({count} borders): {", ".join(neighbors)}')
