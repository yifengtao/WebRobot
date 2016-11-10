import urllib
import sys
import subprocess
print sys.argv[1]
testfile=urllib.URLopener()
cnt=0
label=1
subprocess.call('mkdir '+sys.argv[1],shell=True)
with open(sys.argv[1]+'_log.txt','a') as f_out, open(sys.argv[1]+'_last_2_quarter.txt','r') as f:
    line=f.readline()
    while line:
        tks=line.split('\t')
        print tks[1].strip()
        try: 
            testfile.retrieve(tks[1].strip(),sys.argv[1]+"/"+tks[0]+".jpg")
        except:
            f_out.write(line+"\n")
        line=f.readline()
        cnt+=1
        if cnt%1000==0:
            subprocess.call('./pack_send.sh '+sys.argv[1]+' '+str(label),shell=True)
            label+=1



