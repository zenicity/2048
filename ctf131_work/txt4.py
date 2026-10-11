import numpy as np, pickle
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
W,S=pickle.load(open('WS.pkl','rb'))
rows=range(80,120)
T=np.full((len(rows),128),np.nan)
for ri,g in enumerate(rows):
    cand=[]
    for (bs,sgn) in ((0,1),(3,-1)):
        if (bs,g) in S and (bs,g) in W:
            for s in S[(bs,g)]:
                for w in W[(bs,g)]:
                    d=(s-w)*sgn
                    cand.append(np.where(np.abs(d)<=30,d,np.nan))
    if cand:
        C=np.array(cand)
        with np.errstate(all='ignore'):
            T[ri]=np.nanmedian(C,axis=0)
fig,ax=plt.subplots(1,1,figsize=(22,10))
ax.imshow(T[:,40:128],cmap='gray_r',vmin=0,vmax=12,interpolation='nearest',aspect='equal')
ax.set_yticks(range(0,len(rows),2)); ax.set_yticklabels([str(r) for r in rows][::2])
plt.tight_layout(); plt.savefig('txt4.png',dpi=55)
pickle.dump(T,open('T.pkl','wb'))
