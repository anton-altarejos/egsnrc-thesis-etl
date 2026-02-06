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

for i in {001,003,005,006,007,008,009,010,012,014,016,018,020,022,024,026,028,030,035,040,045,050,055,060,065,070,100} ;
do 
    for j in {nucleus,cytoplasm,membrane,cell}
    do
        cp ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp ..
        #cp ell_mdamb"$model".egsinp ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp;
        cd ..
        rm -f *.egsjob *lock *egsparallel
        count=$(($count+1))
        echo $count" out of 84: egs_chamber -i ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp"
        #echo "egs_chamber -i ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp"
        egs-parallel -n5 -d 1000 -c "egs_chamber -i ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp" ;
        rm -f ell_"$i"_mdamb"$model"_"$j"_"$angle".egsinp *_w*.*
        rm -f *.egsjob *lock *egsparallel
        mv ell_"$i"_mdamb"$model"_"$j"_"$angle".egslog $dir
        end=`date +%s`
        runtime=$(($end-$start))
        echo $runtime
        cd $dir
    done
done
#python3 ell_radionuclides_spectra.py
#python3 ell_extractor.py

cd ..
#mv ell_source_nucleus.csv ell_source_cytoplasm.csv ell_source_membrane.csv ell_source_cell.csv $dir
rm *.geom

end=`date +%s`

runtime=$(($end-$start))
echo $runtime | tee time_ell_mono_mdamb"$model"_"$angle".txt
