'''
Computes monthly precipitation for a given basin, using data from IMERG-Final.
'''

import calendar
import datetime
import glob
import earthaccess
import numpy as np
import h5py
import xarray as xr
import geopandas
from matplotlib import pyplot
from pyproj import CRS

BASIN_FILE = '/home/arthur.endsley/Workspace/NTSG/projects/Y2024_TOPS_Training/data/YellowstoneRiver_drainage_WSG84.shp'

def main():
    auth = earthaccess.login()
    basin = geopandas.read_file(BASIN_FILE)

    results = earthaccess.search_data(
        short_name = 'GPM_3IMERGM',
        temporal = ('2014-01-01', '2023-12-31'))
    earthaccess.download(results, 'data/IMERG-Final_monthly')
    file_list = glob.glob('data/IMERG-Final_monthly/*.HDF5')
    file_list.sort()

    datasets = []
    for i, filename in enumerate(file_list):
        # Only need to do this once, for the first file
        if i == 0:
            with h5py.File(filename, 'r') as hdf:
                longitude = hdf['Grid/lon'][:]
                latitude = hdf['Grid/lat'][:]

        # Read the HDF5 file as an xarray Dataset, clip it to
        #    out basin's boundary
        ds0 = hdf5_to_xarray_dataset(filename, longitude, latitude)
        ds_clip = ds0.rio.clip(basin.geometry.values)
        datasets.append(ds_clip)

    # Merge the datasets together along the "time" axis (i.e., build a time series)
    ds = xr.concat(datasets, dim = 'time')

    # Converting from [mm hour-1] to [mm month-1], then compute basin-wide
    #    monthly precip.
    days_in_month = np.array(calendar.mdays)[ds.coords['time.month'].values]
    ds['precip_monthly'] = ds.precipitation * 24 * days_in_month.reshape((days_in_month.size, 1, 1))
    precip_series = ds.precip_monthly.mean(['lon','lat']).values


def hdf5_to_xarray_dataset(filename, longitude = None, latitude = None):
    '''
    Reads an HDF5 file representing daily data and returns an
    xarray.Dataset with the date, latitude, and longitude coordinates
    properly defined.

    Parameters
    ----------
    filename : str
        The file path to the HDF5 file
    longitude : numpy.ndarray
        The longitude coordinates, as a 1D NumPy array
    latitude : numpy.ndarray
        The latitude coordinates, as a 1D NumPy array

    Returns
    -------
    xarray.Dataset
    '''
    if longitude is None or latitude is None:
        with h5py.File(filename, 'r') as hdf:
            longitude = hdf['Grid/lon'][:]
            latitude = hdf['Grid/lat'][:]

    # Get the date of this image
    date = datetime.datetime.strptime(filename.split('.')[4][0:8], '%Y%m%d')
    ds0 = xr.open_dataset(
        filename, group = 'Grid', decode_times = False).get(['precipitation'])
    # Define the missing coordinates
    ds0 = ds0.assign_coords({
        'time': [date], 'x': longitude, 'y': latitude
    })

    # Define the coordinate reference system (CRS) and the spatial coordinates
    ds0 = ds0.rio.write_crs(CRS.from_epsg(4326))
    ds0 = ds0.rio.set_spatial_dims('lon', 'lat')
    return ds0


if __name__ == '__main__':
    main()
