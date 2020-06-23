""" I/O routines for SST data"""

import os
import numpy as np

import iris

from oceanpy.sphharm import utils


def load_noaa(dmy, nside=None, mask=False):
    """

    Parameters
    ----------
    dmy : tuple  (day, month, year)
    nside : int, optional
    mask : bool, optional

    Returns
    -------
    dmy_cube or SST : iris.Cube or healpy.ma

    """
    # Convenience
    day, month, year = dmy
    # Check
    noaa_path = os.getenv('NOAA_OI')
    if noaa_path is None:
        raise IOError("You muse set the NOAA_OI environmental variable!")
    # Year file
    noaa_file = os.path.join(noaa_path, 'sst.day.mean.{}.nc'.format(year))
    # IRIS
    sst_cube = iris.load(noaa_file, 'sst')[0]

    # Day
    constraint = iris.Constraint(time=iris.time.PartialDateTime(
        day=day, year=year, month=month))
    dmy_cube = sst_cube.extract(constraint)

    # Healpix?
    if nside is None:
        return dmy_cube

    SST, _, _ = utils.cube_to_healpix(nside, dmy_cube, fill_value=-10)

    if mask:
        # Mask
        land_mask = np.zeros_like(SST, dtype='bool')
        land_mask[SST < -5] = True
        SST.mask = land_mask

    # Return
    return SST
