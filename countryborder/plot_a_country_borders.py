import matplotlib.pyplot as plt
import networkx as nx


def plot_a_country_borders(G, country_name):  # noqa
    """
    Plot the borders of a specified country and its neighboring countries on a map.
    Parameters:
    G (networkx.Graph): The network of neighboring countries.
    country_name (str): The name of the country to visualize.
    This function generates a subgraph containing the specified country and its neighboring countries,
    calculates node positions based on latitude and longitude, and visualizes the borders.
    """
    # Create a subgraph containing the specified country and its neighbors
    country_and_neighbors = [node for node in G.neighbors(country_name)] + [country_name]
    subgraph = G.subgraph(country_and_neighbors)

    # Calculate node positions using latitude and longitude
    node_positions = {n: (d['longitude'], d['latitude']) for n, d in subgraph.nodes(data=True)}

    # Visualize the subgraph with specified node and edge attributes
    nx.draw(
        subgraph,
        pos=node_positions,
        with_labels=True,
        node_size=200,
        font_size=10,
        node_color='hotpink',
        edge_color='gray',
    )

    # Set the plot title
    plt.title(f"Network of Country Borders in {country_name}", fontsize=18)

    # Turn off the axis labels and ticks
    plt.axis('off')

    # Display the plot
    plt.show()


# Call the function to plot the Mexico borders
# plot_country_borders(G, 'Mexico')
