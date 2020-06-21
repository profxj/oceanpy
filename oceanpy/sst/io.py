""" I/O routines for SST data"""

import os

import iris


def load_noaa(dmy):
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

    # Return
    return dmy_cube
