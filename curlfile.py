with open('filename.txt') as f:
    for line in f:
        line = line.strip()
        print 'echo \''+line+'\''
        print 'curl '+'\'ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF/'+line+'.sdf.gz\' -o '+line+'.sdf.gz'
        #print 'tar -zxvf '+line+'.sdf.gz '+line+'.sdf'
        #print 'rm '+line+'.sdf.gz'
        #print '../smina.static -r '
        print '../smina.static --autobox_ligand ../localData/raw/1ca9_lig.sdf -r ../localData/raw/1ca9_rec.pdb -l '+line+'.sdf.gz -o '+line+'.sdf > log.txt'
        print '../sdsorter.static -sort minimizedAffinity -reduceconfs 1 -nbest 1000 '+line+'.sdf'+' '+line+'_refined.sdf'
        print 'rm '+line+'.sdf.gz'
        print 'rm '+line+'.sdf'


