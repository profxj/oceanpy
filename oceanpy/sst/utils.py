""" Utilities for SST data and analysis"""
import numpy as np

#import iris
#from cf_units import Unit

def noaa_oi_coords(as_iris_coord=False):
    """
    Return the default spatial coords for NOAA OI data

    Parameters
    ----------
    as_iris_coord : bool, optional
        Return as Iris.coords.DimCoord instead of np.ndarray

    Returns
    -------
    lat, lon : np.ndarray or iris.coords.DimCoord
        latitude values, longitude values

    """
    # Simply calculate
    lat = -89.875 + np.arange(720)*0.25
    lon = 0.125 + np.arange(1440)*0.25

    # Convert to an Iris coord?
    if as_iris_coord:
        lat = iris.coords.DimCoord(lat, standard_name='latitude', units=Unit('degrees'),
                                   long_name='Latitude')
        lon = iris.coords.DimCoord(lon, standard_name='longitude', units=Unit('degrees'),
                                   long_name='Longitude')
    # Return
    return lat, lon
