import networkx as nx


def create_country_network(gdf, country_column):
    """
    Create a network of neighboring countries based on their geometries and attributes.
    Parameters:
    gdf (geopandas.GeoDataFrame): A GeoDataFrame containing country geometries and attributes.
    country_column (str): The name of the column in the GeoDataFrame that contains country names.
    Returns:
    networkx.Graph: A NetworkX graph representing countries as nodes and neighboring relationships as edges.
    The function validates and cleans the input geometries, extracts latitude and longitude,
    adds countries as nodes to the graph, and adds edges between neighboring countries.

    """
    # Initialize a NetworkX graph
    G = nx.Graph()  # noqa

    # Validate and clean geometries
    for idx, row in gdf.iterrows():
        country_name = row[country_column]
        geom = row['geometry']

        # Validate the geometry
        if not geom.is_valid:
            # Buffer with a very small distance to fix invalid geometries
            geom = geom.buffer(0)

        # Add the cleaned geometry back to the GeoDataFrame
        gdf.at[idx, 'geometry'] = geom

        # Extract latitude and longitude from the GeoDataFrame
        latitude = row['latitude']
        longitude = row['longitude']

        # Add the country as a node in the NetworkX graph with latitude and longitude as attributes
        G.add_node(country_name, latitude=latitude, longitude=longitude)

    # Add edges between neighboring countries
    for idx, row in gdf.iterrows():
        country1 = row[country_column]
        geom1 = row['geometry']

        for idx2, row2 in gdf.iterrows():
            if idx != idx2:
                country2 = row2[country_column]
                geom2 = row2['geometry']

                # Check if the cleaned geometries intersect
                if geom1.intersects(geom2):
                    G.add_edge(country1, country2)

    return G
