from multiprocessing import Pool
import subprocess

lut = ['Compound_000000001_000025000','Compound_002500001_002525000']
def f(content):
    subprocess.call('../smina.static --autobox_ligand ../localData/raw/1ca9_lig.sdf -r ../localData/raw/1ca9_rec.pdb -l '+content+'.sdf.gz -o '+content+'.sdf --exhaustiveness 1', shell=True)

def f1():
    subprocess.call('../smina.static --autobox_ligand ../localData/raw/1ca9_lig.sdf -r ../localData/raw/1ca9_rec.pdb -l Compound_000000001_000025000.sdf.gz -o Compound_000000001_000025000.sdf --exhaustiveness 1', shell=True)

pool = Pool(processes=2)
pool.map(f,lut)
#out1 = pool.apply_async(f1())
#out2 = pool.appy_async(f2())
#pool.close()
#pool.join()
#final = FinalProcess(out1,out2)
#subprocess.call(['../smina.static','--autobox_ligand','../localData/raw/1ca9_lig.sdf','-r','../localData/raw/1ca9_rec.pdb','-l','Compound_000000001_000025000.sdf.gz','-o','Compound_000000001_000025000.sdf'])
#subprocess.call(['../smina.static','--autobox_ligand','../localData/raw/1ca9_lig.sdf','-r','../localData/raw/1ca9_rec.pdb','-l','Compound_002500001_002525000.sdf.gz','-o','Compound_002500001_002525000.sdf.gz'])
