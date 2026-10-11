import numpy as np, pickle
from lora import *
out=pickle.load(open('bursts.pkl','rb'))
allr=[]
for st,en,a,pw,syms in out:
    pre=syms[0]
    r=getsyms(a,pre,230)
    # SFD down check for sanity
    allr.append(((st,en,a,pw,pre),[(v-pre)%N for v in r]))
pickle.dump(allr,open('allr.pkl','wb'))
print(len(allr))
for k in (0,1,2,3):
    print(allr[k][0],allr[k][1][:20])
