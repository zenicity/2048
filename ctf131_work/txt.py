import numpy as np, pickle
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
exec(open('full.py').read().split("out=[]")[0])
res=pickle.load(open('res4.pkl','rb'))
W={};S={}
for k,r in enumerate(res):
    if len(r['ds'])<200: continue
    rr=[int(round(v))%128 for v in r['ds']]
    hn,ln,cr,crc,by=decode(rr)
    if len(by)<136: continue
    key=(by[6],by[7])
    if by[:2]!=b'AL' or by[6]>4 or by[7]>127: continue
    D=S if r['pw']>20 else W
    D.setdefault(key,[]).append(np.frombuffer(by[8:136],dtype=np.uint8).astype(float))
pickle.dump((W,S),open('WS.pkl','wb'))
print(len(W),len(S))
fig,ax=plt.subplots(1,2,figsize=(18,9))
for j,b in enumerate((0,3)):
    M=np.full((128,128),np.nan)
    for g in range(128):
        if (b,g) in S and (b,g) in W:
            best=None
            for s in S[(b,g)]:
                for w in W[(b,g)]:
                    d=s-w; sc=np.sum(np.abs(d)<=25)
                    if best is None or sc>best[0]: best=(sc,d)
            d=best[1]; M[g]=np.where(np.abs(d)<=25,d,np.nan)
    ax[j].imshow(M,cmap='bwr',vmin=-20,vmax=20,interpolation='nearest'); ax[j].set_title(f'band {b}')
plt.savefig('txt.png',dpi=55)
