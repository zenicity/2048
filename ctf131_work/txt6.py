import numpy as np, pickle
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
F=pickle.load(open('F.pkl','rb'))
rows=range(80,120)
T=np.full((len(rows),128),np.nan)
for ri,g in enumerate(rows):
    cand=[]
    for bs,sgn in ((0,1),(3,-1)):
        for (sv,st) in F.get(('S',bs,g),[]):
            for (wv,wt) in F.get(('W',bs,g),[]):
                ok=st&wt
                d=np.where(ok,(sv-wv)*sgn,np.nan)
                cand.append(d)
    if cand:
        with np.errstate(all='ignore'):
            T[ri]=np.nanmedian(np.array(cand),axis=0)
pickle.dump(T,open('T2.pkl','wb'))
sub=T[84-80:116-80,50:120]
cl=np.where(np.isnan(sub),0.5,np.clip(sub,0,13)/13)  # nan -> grey .5? show separately
fig,ax=plt.subplots(1,1,figsize=(21,10))
img=np.where(np.isnan(sub),np.nan,1-np.clip(sub,0,13)/13)
ax.imshow(np.ma.masked_invalid(img),cmap='gray',vmin=0,vmax=1,interpolation='nearest',extent=[50,120,116,84])
ax.set_facecolor('#88aaff')
ax.set_xticks(range(50,120,2)); ax.set_yticks(range(84,116)); ax.tick_params(labelsize=7)
plt.tight_layout(); plt.savefig('txt6.png',dpi=60)
