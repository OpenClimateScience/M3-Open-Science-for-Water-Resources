'''
For more information:

    https://osf.io/rpc3w/
'''

import xarray as xr

OUTPUT_FILE = '/home/arthur/Workspace/NTSG/projects/Y2024_TOPS_Training/data/HYSETS-2023_watershed_YellowstoneRiver.nc'
HYSETS_DATASET = '/home/arthur.endsley/Downloads/TOPS/HYSETS_2023_update_QC_stations.nc'
STATION_IDX = [
    # (8753, 'KansasRiver'),
    (8209, 'YellowstoneRiver'),
] # Corresponding to WatershedID 8210, 8754 (index is one less)

def main():
    hysets = xr.open_dataset(HYSETS_DATASET)
    datasets = []
    for sid, name in STATION_IDX:
        ds = dict()
        for key in ('discharge', 'total_precipitation', '2m_tasmax', '2m_tasmin', 'drainage_area', 'slope', 'elevation'):
            ds[key] = hysets[key].loc[sid]

        ds = xr.Dataset(ds)
        datasets.append(ds)

    ds_combined = xr.concat(datasets, dim = 'id')
    ds.to_netcdf(OUTPUT_FILE)


if __name__ == '__main__':
    main()
