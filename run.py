from multiprocessing import Pool
import subprocess
import glob,os

# function of calculating the sdf from the file fn.
def f(fn):
    subprocess.call('../smina.static --autobox_ligand ../localData/raw/1ca9_lig.sdf -r ../localData/raw/1ca9_rec.pdb -l inputData/'+fn+'.sdf.gz -o outputData/'+fn+'.sdf --exhaustiveness 1 > outputData/log_'+fn+'.txt', shell=True)
    subprocess.call('../sdsorter.static -sort minimizedAffinity -reduceconfs 1 -nbest 1000 outputData/'+fn+'.sdf refinedData/'+fn+'_refined.sdf', shell=True)

# read into the filenames.
filename = list()
os.chdir('inputData')
for file in glob.glob('*.sdf.gz'):
    filename.append(file[:-7])
os.chdir('..')

# distribute the task to 29 threads.
pool = Pool(processes=29)
pool.map(f,filename)
