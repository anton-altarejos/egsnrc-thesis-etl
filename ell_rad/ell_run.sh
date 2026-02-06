#!/bin/bash

# This bash file makes several copies of a base .egsinp file

# 3 cell models
#cp sph_spectra.egsinp sph_mdamb468.egsinp
#cp sph_spectra.egsinp sph_mdamb361.egsinp
#cp sph_spectra.egsinp sph_mdamb231.egsinp

start=`date +%s`
dir="$(pwd)"
model="${dir:${#dir}-6:3}"
angle="${dir:${#dir}-2:3}"
count=0;

cp *.geom ..

for i in {tc99m,in111,i123,i125,tl201} ; 
do 
    for j in {nucleus,cytoplasm,membrane,cell}
    do
        cp ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp ..
        #cp ell_mdamb"$model".egsinp ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp;
        cd ..
        rm -f *.egsjob *lock *egsparallel
        count=$(($count+1))
        echo $count" out of 20: egs_chamber -i ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp"
        #echo "egs_chamber -i ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp"
        egs-parallel -n5 -d 1000 -c "egs_chamber -i ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp" ;
        rm -f ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp *_w*.*
        rm -f *.egsjob *lock *egsparallel
        mv ell_"$i"_mdamb"$model"_"$j"_"$angle".egslog $dir
        
        cd $dir
    done
done
#python3 ell_radionuclides_spectra.py
python3 ell_extractor.py

cd ..
#mv ell_source_nucleus.csv ell_source_cytoplasm.csv ell_source_membrane.csv ell_source_cell.csv $dir
rm *.geom

end=`date +%s`

runtime=$(($end-$start))
echo $runtime | tee time_ell_rad_mdamb"$model"_"$angle".txt
