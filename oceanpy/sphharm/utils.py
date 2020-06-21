""" Utility routines for Spherical Harmonic analysis """
import numpy as np
from scipy import interpolate

import healpy as hp


def cube_to_healpix(nside, cube, fill_value=-1e9):
    """
    Interpolate a rectilinear map from an IRIS Cube onto a Healpy map
    Uses Rectilinear Bivariate Spline from scipy

    Args:
        nside (int):  Should be a power of 2, e.g. 256
        cube (iris.Cube):
        fill_value (float, optional):

    Returns:
        tuple:  np.ndarray, np.ndarray, np.ndarray
            data in healpy
            theta values in deg
            phi values in deg

    """
    npix_hp = hp.nside2npix(nside)
    lat_coord = cube.coord('latitude').points
    lon_coord = cube.coord('longitude').points
    #
    data = cube.data[:]
    data.fill_value = fill_value
    # Coords
    theta, phi = np.degrees(hp.pix2ang(nside=nside, ipix=np.arange(npix_hp)))

    # Interpolate
    func = interpolate.RectBivariateSpline(lat_coord, lon_coord, data.filled(),
                                           kx=2, ky=2)  # , epsilon=2)
    SST = func.ev(90 - theta, phi)

    # hp
    hp_SST = hp.ma(SST)

    # Return
    return hp_SST, theta, phi
