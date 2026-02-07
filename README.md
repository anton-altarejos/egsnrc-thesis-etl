# egsnrc-thesis-etl
Automation script I wrote for my undergraduate thesis. A default installation of the egs_chamber tool from the EGSnrc toolkit does not outright support multiple sequential simulations. I needed simulations with varying electron source energies and localization so I wrote BASH and Python scripts that did this for me. It involves the creation of the simulation geometries up to the creating of organized datasets containing the S-values. 

**SPECIFIC VALUES AND SPECIFICATIONS HAVE BEEN REDACTED TO PROTECT THE INTELLECTUAL PROPERTY OF THE AUTHOR**

## How to use
Simply copy the files into `egs_chamber/` and you should be able to run the shell scripts directly.

### 

## Some notes
The `sph` scripts are immediately ready to be run. However, the `ell` scripts need the `copybase` scripts ran first since the ellipsoid geometries are more complicated.

The `.ipynb` files are obviously for reading the datasets generated and turning them into the necessary plots.
