# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
Coriolis forces
"""
import numpy as np
import unyt


def coriolis_parameter(latitude):
    f = 2 * unyt.Omega_earth * np.sin(latitude)
    # Return
    return f


def meridional_derivative(latitude):
    beta = (2*unyt.Omega_earth/unyt.R_Earth) * np.cos(latitude)
    # Return
    return beta.to('1/km/s')

