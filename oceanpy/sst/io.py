""" I/O routines for SST data"""

import os
import numpy as np
import datetime

import xarray

from oceanpy.sphharm import utils
from oceanpy.sst import climate

from IPython import embed


def load_noaa(dmy, nside=None, mask=False, subtract_seasonal=False,
              ret_angles=False, climate_file=None):
    """

    Parameters
    ----------
    dmy : tuple  (day, month, year)
    nside : int, optional
        If provided, convert into a healpix
    mask : bool, optional
    subtract_seasonal : bool, optional
        Subtract off the seasonal average?
    ret_angles : bool, optional

    Returns
    -------
    dmy_cube or SST : xarray.DataArray or healpy.ma
    if ret_angles:
       theta, phi

    """
    # Convenience
    day, month, year = dmy
    time = datetime.datetime(day=day, month=month, year=year)
    # Check
    noaa_path = os.getenv('NOAA_OI')
    if noaa_path is None:
        raise IOError("You muse set the NOAA_OI environmental variable!")
    # Year file
    noaa_file = os.path.join(noaa_path, 'sst.day.mean.{}.nc'.format(year))

    # xarray
    ds = xarray.open_dataset(noaa_file)

    # Day
    #constraint = iris.Constraint(time=iris.time.PartialDateTime(
    #    day=day, year=year, month=month))
    #dmy_cube = sst_cube.extract(constraint)
    dmy_SST = ds.sst.sel(time=time)

    # Seasonal?
    if subtract_seasonal:
        dt = datetime.datetime(year=dmy[2], month=dmy[1], day=dmy[0])
        day_of_year = (dt - datetime.datetime(dt.year, 1, 1)).days + 1
        # Leap year?
        if (year % 4) != 0:
            if day_of_year <= 28:
                pass
            else:
                day_of_year += 1
        #
        Tday = climate.noaa_climate_day(day_of_year, climate_file=climate_file)
        dmy_SST -= Tday

    # Healpix?
    if nside is None:
        return dmy_SST

    # More Refactoring needed
    import pdb; pdb.set_trace()

    SST, theta, phi = utils.cube_to_healpix(nside, dmy_cube, fill_value=-10)

    if mask:
        # Mask
        land_mask = np.zeros_like(SST, dtype='bool')
        land_mask[SST < -5] = True
        SST.mask = land_mask

    # Return
    if ret_angles:
        return SST, theta, phi
    else:
        return SST
