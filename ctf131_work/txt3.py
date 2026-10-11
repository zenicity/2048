import numpy as np, pickle
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
W,S=pickle.load(open('WS.pkl','rb'))
M=np.full((128,128),np.nan)
for g in range(128):
    if (0,g) in S and (0,g) in W:
        best=None
        for s in S[(0,g)]:
            for w in W[(0,g)]:
                d=s-w; sc=np.sum(np.abs(d)<=3)
                if best is None or sc>best[0]: best=(sc,d)
        M[g]=best[1]
fig,ax=plt.subplots(1,2,figsize=(18,9))
ax[0].imshow(M,cmap='bwr',vmin=-120,vmax=120,interpolation='nearest')
ax[1].imshow(np.where(M<-25,1,np.where(np.isnan(M),np.nan,0)),cmap='gray_r',interpolation='nearest')
plt.savefig('txt3.png',dpi=55)
