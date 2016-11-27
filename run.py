from multiprocessing import Pool
import subprocess
import glob,os
import random

# function for multi-thread processing.
def f(fn):
    # download the file from PubChem according to filename(fn).
    subprocess.call("curl 'ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF/"+fn+".sdf.gz' -o inputData/"+fn+".sdf.gz", shell=True)
    # limit the weight of molecular(< 501 MW) before docking.
    subprocess.call("../sdsorter.static -max 'molecular weight',501 -reduceconfs 1 -nbest 50000 inputData/"+fn+".sdf.gz inputData/"+fn+"_wt.sdf", shell=True)
    # main part: redock the lig to the rec.
    subprocess.call('../smina.static --autobox_ligand ../raw/3BEJ_lig_edit.sdf -r ../raw/3BEJ_REC.pdb -l inputData/'+fn+'_wt.sdf -o outputData/'+fn+'.sdf --exhaustiveness 1 > outputData/log_'+fn+'.txt', shell=True)
    # sort and refine the generated *.sdf file.
    subprocess.call('../sdsorter.static -sort minimizedAffinity -reduceconfs 1 -nbest 1000 outputData/'+fn+'.sdf outputData/'+fn+'_refined.sdf', shell=True)
    # remove unrefined generated data, raw lig file, weight-limited raw lig file.
    subprocess.call('rm outputData/'+fn+'.sdf', shell=True)
    subprocess.call('rm inputData/'+fn+'.sdf.gz', shell=True)
    subprocess.call('rm inputData/'+fn+'_wt.sdf', shell=True)

# read into the filenames.
filename = list()
fop = open('filename_full.txt', 'r')
for line in fop:
    filename.append(line.strip())
fop.close()

# shuffle filenames.
random.seed(6)
random.shuffle(filename)

# distribute the task to 28 threads.
pool = Pool(processes=28)
pool.map(f,filename)
# EOF.
