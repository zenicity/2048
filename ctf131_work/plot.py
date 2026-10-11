import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
S=np.load('S.npy'); P=10*np.log10(S+1)
# average over time blocks of 8 rows
n=P.shape[0]//16*16
Q=P[:n].reshape(-1,16,P.shape[1]).mean(1)
plt.figure(figsize=(14,10)); plt.imshow(Q,aspect='auto',extent=[-1000,1000,50.7,0],vmin=np.percentile(Q,5),vmax=np.percentile(Q,99.8)); plt.xlabel('kHz'); plt.ylabel('s'); plt.colorbar(); plt.savefig('wf.png',dpi=70)
