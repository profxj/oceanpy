import matplotlib.ticker as mticker

import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


def draw_gridlines(ax, lw=2):
    # Gridlines
    # https://stackoverflow.com/questions/49956355/adding-gridlines-using-cartopy
    gl = ax.gridlines(crs=ccrs.PlateCarree(), linewidth=lw, color='black', alpha=0.5,
                      linestyle='--', draw_labels=True)
    gl.xlabels_top = False
    gl.ylabels_left = True
    gl.ylabels_right=False
    gl.xlines = True
    #gl.ylines = True
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'color': 'black', 'weight': 'bold'}
    gl.ylabel_style = {'color': 'black', 'weight': 'bold'}

    #gl.xlocator = mticker.FixedLocator([-240., -180., -120, -60, 0, 60, 120.])
    #gl.ylocator = mticker.FixedLocator([0., 15., 30., 45, 60.])
