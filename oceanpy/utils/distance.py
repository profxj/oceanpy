""" Basic distance calculations """

import numpy as np
import unyt

def ang_to_size(angle, lat):
    circ = 2*np.pi*1*unyt.R_Earth

    # Latitude -- independent of lat!
    lat_km_deg = circ / (360. * unyt.deg)

    # Long
    circp = circ * np.cos(lat)
    lon_km_deg = circp / (360. * unyt.deg)

    # Return
    return (angle*lon_km_deg).to('km'), (
        angle*lat_km_deg).to('km')