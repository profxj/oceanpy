""" Utility routines for Spherical Harmonic analysis """
import numpy as np
from scipy import interpolate

import healpy as hp


def cube_to_healpix(nside, cube):
    """
    Interpolate a rectilinear map from an IRIS Cube onto a Healpy map
    Uses Rectilinear Bivariate Spline from scipy

    Args:
        nside (int):  Should be a power of 2, e.g. 256
        cube (iris.Cube):

    Returns:
        tuple:  np.ndarray, np.ndarray, np.ndarray
            SST in healpy
            theta values in deg
            phi values in deg

    """
    npix_hp = hp.nside2npix(nside)
    lat_coord = cube.coord('latitude').points
    lon_coord = cube.coord('longitude').points
    #
    sst = cube.data[:]
    sst.fill_value = -10
    # Coords
    theta, phi = np.degrees(hp.pix2ang(nside=nside, ipix=np.arange(npix_hp)))

    # Interpolate
    func = interpolate.RectBivariateSpline(lat_coord, lon_coord, sst.filled(),
                                           kx=2, ky=2)  # , epsilon=2)
    SST = func.ev(90 - theta, phi)

    # Return
    return SST, theta, phi
