M3: Open Science for Water Resources
====================================

> What tools and datasets are available to quantify water quantity and availability?

The third module of our [open climate-science curriculum](https://openclimatescience.github.io/curriculum) focuses on how to begin a reproducible computational science project, using water resources as a thematic example. **At the end of this module, you should be able to:**

- Describe the major fluxes and pools of the terrestrial water cycle;
- Know where to access remotely sensed or modeled data on water storage anomalies, evapotranspiration, and soil moisture;
- Calculate a water budget.


Contents
--------------

1. Creating a Research Software Environment


Getting Started
---------------

[See our installation guide here.](https://github.com/OpenClimateScience/M1-Open-Climate-Data/blob/main/HOW_TO_INSTALL.md)

You can run the notebooks in this repository using [Github Codespaces](https://docs.github.com/en/codespaces/overview) or as [a VSCode Dev Container](https://code.visualstudio.com/docs/devcontainers/containers). Once your container is running, launch Jupyter Notebook by:

```sh
# Create your own password when prompted
jupyter server password

# Then, launch Jupyter Notebook; enter your password when prompted
jupyter notebook
```

**The Python libraries required for the exercises can be installed using the `pip` package manager:**

```sh
pip install xarray netcdf4 dask
```


Learning Outcomes
-----------------

- Chooses meaningful filenames (CC1.3)
- Records relationships between code, results, and metadata (CC1.5)
- Uses a package manager to install and manage software dependencies (CC1.10)
- Understands multi-dimensional arrays (CC2.3)
- Can scale up a computational workflow (CC2.6)
- Chooses variable names that are clear and informative (CC3.8)
- Uses assertions to verify assumptions as runtime (CC4.7)
- Writes short, simple functions that have no side effects (CC4.9)


Climate Datasets Used
---------------------

- [Terrestrial water storage anomalies from the NASA GRACE and GRACE-FO missions](https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.1_V3)


Acknowledgements
----------------

This curriculum was enabled by a grant from NASA's Transition to Open Science (TOPS) Training program (80NSSC23K0864), part of [NASA's TOPS Program](https://nasa.github.io/Transform-to-Open-Science/)
