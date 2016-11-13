cat *.sdf > refine1.sdf
../sdsorter.static -sort minimizedAffinity -reduceconfs 1 -nbest 200 refine1.sdf refine2.sdf
../smina.static --autobox_ligang ../localData/raw/1ca8_lig.sdf -r ../localData/raw/1ca8_rec.pdb -l refine2.sdf -o refine3.sdf --exhaustiveness 1
