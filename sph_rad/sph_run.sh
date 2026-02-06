#!/bin/bash

# This bash script automates the process of running each individual .egsinp file
# through the Monte Carlo simulation then moves their results to a dump folder for further processing
#
# Parameters: 10 cores used, 10 second delay between each set(source region category)
# take egsinp files from inside sph_rad/ then return

start=`date +%s`
start=`date +%s`
dir="$(pwd)"
count=0;




#sph_in111_mdamb231_cytoplasm.egsinp
for k in {361,468};
do
    for i in {i123,i125,tl201,tc99m,in111} ;
    do 
        for j in {nucleus,cytoplasm,membrane,cell}
        do
            #cp sph_mdamb468.egsinp sph_"$i"_mdamb468_"$j".egsinp
            #cp sph_mdamb361.egsinp sph_"$i"_mdamb361_"$j".egsinp
            #cp sph_mdamb231.egsinp sph_"$i"_mdamb231_"$j".egsinp
            cp sph_"$i"_mdamb"$k"_"$j".egsinp ..
            cd ..
            rm -f *.egsjob *lock *egsparallel
            count=$(($count+1))
            echo $count" out of 60: egs_chamber -i sph_"$i"_mdamb"$k"_"$j".egsinp"
            egs-parallel -n5 -d 1000 -c "egs_chamber -i sph_"$i"_mdamb"$k"_"$j".egsinp " ;
            rm -f sph_"$i"_mdamb"$k"_"$j".egsinp *_w*.*
            rm -f *.egsjob *lock *egsparallel
            mv sph_"$i"_mdamb"$k"_"$j".egslog $dir
        
            cd $dir
    
        done
    done
done

rm *.egsjob *.egsparallel *_w*
#mv sph_*_mdamb* sph_rad/

end=`date +%s`

runtime=$(($end-$start))
echo $runtime

