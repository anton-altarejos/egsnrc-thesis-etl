#!/bin/bash

# This bash file makes several copies of a base .egsinp file

# 3 cell models
#cp sph_spectra.egsinp sph_mdamb468.egsinp
#cp sph_spectra.egsinp sph_mdamb361.egsinp
#cp sph_spectra.egsinp sph_mdamb231.egsinp


dir="$(pwd)"
model="${dir:${#dir}-6:3}"
angle="${dir:${#dir}-2:3}"

for i in {001,003,005,006,007,008,009,010,012,014,016,018,020,022,024,026,028,030,035,040,045,050,055,060,065,070,100} ; 
do 
    for j in {nucleus,cytoplasm,membrane,cell}
    do
        cp ell_mdamb"$model".egsinp ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp
    done
done
#python3 ell_radionuclides_spectra.py
