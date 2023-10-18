import matplotlib.pyplot as plt
import networkx as nx


def plot_country_network_on_map(gdf, G):  # noqa
    """
    Plot a network of neighboring countries on a map.
    Parameters:
    gdf (geopandas.GeoDataFrame): A GeoDataFrame containing country geometries and attributes.
    G (networkx.Graph): The network of neighboring countries.
    This function creates a plot with a background map, overlays the network of neighboring countries,
    and displays the result.
    """
    ax = plot_background(gdf)

    # Create a dictionary of node positions using longitude and latitude
    node_positions = {n: (d['longitude'], d['latitude']) for n, d in G.nodes(data=True)}

    # Draw the network on the map with specified node and edge attributes
    nx.draw(
        G,
        pos=node_positions,
        with_labels=False,  # Do not display node labels
        node_size=5,       # Set node size
        node_color='maroon',  # Set node color
        edge_color='hotpink',  # Set edge color
        ax=ax
    )

    # Set the plot title
    plt.title("Network of Country Borders with Map Background")

    plt.show()


def plot_background(gdf):
    fig, ax = plt.subplots(figsize=(10, 10))

    ax = gdf.plot(ax=ax, color='palegoldenrod')
    gdf.boundary.plot(ax=ax, linewidth=0.5, color='grey')

    plt.axis('off')

    return ax
