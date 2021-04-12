""" Module for climate routines related to SST.  Mainly NOAA"""
import os
import xarray


def noaa_climate_day(doy, climate_file=None, threshT=False):
    """
    Return the SST for a given day of the year.

    Default is from the 30 years spanning 1983-2012 in the NOAA OI

    Parameters
    ----------
    doy : int
    threshT : bool, optional
        If True, return Tthresh instead of seasonalT

    Returns
    -------
    Tday : xarray.DataSet
        Seasonal T (climatology) if Tthresh is False else Tthresh

    """
    if climate_file is None:
        noaa_path = os.getenv('NOAA_OI')
        if noaa_path is None:
            raise IOError("You muse set the NOAA_OI environmental variable!")
        # Load
        climate_file = os.path.join(os.getenv('NOAA_OI'), 'NOAA_OI_climate_1983-2012.nc')
    #seasonalT = iris.load(climate_file, 'seasonalT')[0]
    ncep_climate = xarray.open_dataset(climate_file)
    if not threshT:
        Tday = ncep_climate.seasonalT.sel(day=doy-1) #  Should be updated
    else:
        Tday = ncep_climate.threshT.sel(day=doy-1) #  Should be updated

    # Return
    return Tday


