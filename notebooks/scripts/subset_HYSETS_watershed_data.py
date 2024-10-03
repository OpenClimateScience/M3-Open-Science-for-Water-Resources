import xarray as xr

OUTPUT_FILE = '/home/arthur/Workspace/NTSG/projects/Y2024_TOPS_Training/data/HYSETS_watershed_YellowstoneRiver.nc'
HYSETS_DATASET = '/home/arthur.endsley/Downloads/TOPS/HYSETS_2020_QC_stations.nc'
STATION_IDX = 8209 # Corresponding to WatershedID 8210 (index is one less)

def main():
    hysets = xr.open_dataset(HYSETS_DATASET)
    ds = dict()
    for key in ('discharge', 'pr', 'tasmax', 'tasmin', 'slope', 'elevation'):
        ds[key] = hysets[key].loc[STATION_IDX]

    ds = xr.Dataset(ds)
    ds.to_netcdf(OUTPUT_FILE)


if __name__ == '__main__':
    main()
