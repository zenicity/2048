import numpy as np, pickle
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
W,S=pickle.load(open('WS.pkl','rb'))
def diffimg(b,sign):
    M=np.zeros((128,128)); cnt=np.zeros((128,128))
    for g in range(128):
        if (b,g) in S and (b,g) in W:
            best=None
            for s in S[(b,g)]:
                for w in W[(b,g)]:
                    d=s-w; sc=np.sum(np.abs(d)<=25)
                    if best is None or sc>best[0]: best=(sc,d)
            d=best[1]; ok=np.abs(d)<=25
            M[g]=np.where(ok,d,0)*sign; cnt[g]=ok
    return M
A=diffimg(0,1); B=diffimg(3,-1)
T=np.clip((A+B)/2,0,None)
fig,ax=plt.subplots(3,1,figsize=(20,14))
ax[0].imshow(A[82:118,45:128],cmap='gray_r',vmin=0,vmax=14,interpolation='nearest',aspect='equal')
ax[1].imshow(B[82:118,45:128],cmap='gray_r',vmin=0,vmax=14,interpolation='nearest',aspect='equal')
ax[2].imshow(np.maximum(A,B)[82:118,45:128],cmap='gray_r',vmin=0,vmax=14,interpolation='nearest',aspect='equal')
plt.tight_layout(); plt.savefig('txt2.png',dpi=60)
