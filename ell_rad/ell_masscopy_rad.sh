#!/bin/bash

# This bash file makes several copies of a base .egsinp file

# 3 cell models
#cp sph_spectra.egsinp sph_mdamb468.egsinp
#cp sph_spectra.egsinp sph_mdamb361.egsinp
#cp sph_spectra.egsinp sph_mdamb231.egsinp


dir="$(pwd)"
model="${dir:${#dir}-6:3}"
angle="${dir:${#dir}-2:3}"

for i in {tc99m,in111,i123,i125,tl201} ; 
do 
    for j in {nucleus,cytoplasm,membrane,cell}
    do
        cp ell_mdamb"$model".egsinp ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp
    done
done
#python3 ell_radionuclides_spectra.py
