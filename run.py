from multiprocessing import Pool
import subprocess
import glob,os
import random

# TODO: remember to limit the weight of molecular before docking
# function of calculating the sdf from the file fn.
def f(fn):
    subprocess.call('curl \'ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/SDF/'+fn+'.sdf.gz\' -o inputData/'+fn+'.sdf.gz')
    subprocess.call('../smina.static --autobox_ligand ../raw/3BEJ_lig_edit.sdf -r ../raw/3BEJ_REC.pdb -l inputData/'+fn+'.sdf.gz -o outputData/'+fn+'.sdf --exhaustiveness 1 > outputData/log_'+fn+'.txt', shell=True)
    subprocess.call('../sdsorter.static -sort minimizedAffinity -reduceconfs 1 -nbest 1000 outputData/'+fn+'.sdf outputData/'+fn+'_refined.sdf', shell=True)

# read into the filenames.
filename = list()
fop = open('filename_full.txt', 'r')
for line in fop:
    filename.append(line.strip())
# shuffle filenames
random.seed(6)
random.shuffle(filename)


#os.chdir('inputData')
#for file in glob.glob('*.sdf.gz'):
#    filename.append(file[:-7])
#os.chdir('..')

# distribute the task to 29 threads.
pool = Pool(processes=1)
pool.map(f,filename)
