from countryborder.country_codes import EXCLUDE


def remove_countries(gdf,
                     countries_to_exclude: list[str]):
    gdf = gdf[~(gdf.ISO_A3 == '-99')]
    return gdf[~gdf.ISO_A3.isin(countries_to_exclude)]


def tidy_data(gdf):
    gdf = remove_countries(gdf, EXCLUDE)

    # gdf = gdf.to_crs('epsg:3857')  # Mecator

    return gdf


def add_centroid(gdf):
    # Calculate the centroid of each polygon and extract the latitude and longitude
    gdf['centroid'] = gdf['geometry'].centroid
    gdf['latitude'] = gdf['centroid'].y
    gdf['longitude'] = gdf['centroid'].x

    # Drop the 'centroid' column if you no longer need it
    gdf = gdf.drop(columns=['centroid'])

    return gdf
