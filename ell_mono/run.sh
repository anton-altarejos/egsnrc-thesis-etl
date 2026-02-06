#!/bin/bash

python3 find.py
python3 build_ellipsoids.py
bash ell_masscopy_mono.sh
python3 ell_energies.py
bash ell_run.sh
python3 ell_extractor.py
python3 yield.py
