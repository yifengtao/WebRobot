from multiprocessing import Pool
import subprocess
import glob,os

def f(fn):
    subprocess.call('../smina.static --autobox_ligand ../localData/raw/1ca9_lig.sdf -r ../localData/raw/1ca9_rec.pdb -l inputData/'+fn+'.sdf.gz -o outputData/'+fn+'.sdf --exhaustiveness 1 > outputData/log_'+fn+'.txt', shell=True)
    subprocess.call('../sdsorter.static -sort minimizedAffinity -reduceconfs 1 -nbest 1000 outputData/'+fn+'.sdf refinedData/'+fn+'_refined.sdf', shell=True)

filename = list()
os.chdir('inputData')
for file in glob.glob('*.sdf.gz'):
    filename.append(file[:-7])
os.chdir('..')


pool = Pool(processes=29)
pool.map(f,filename)



