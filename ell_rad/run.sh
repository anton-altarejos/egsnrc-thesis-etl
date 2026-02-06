#!/bin/bash

python3 find.py
python3 build_ellipsoids.py
bash ell_masscopy_rad.sh
python3 ell_radionuclides_spectra.py
bash ell_run.sh
python3 yield.py