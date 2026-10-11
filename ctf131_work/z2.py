import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fs=1999999.0
off=5.19
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*0.08),offset=2*int(fs*off))
x=d[0::2]+1j*d[1::2]
fig,ax=plt.subplots(2,1,figsize=(14,10))
ax[0].specgram(x,NFFT=128,Fs=fs,noverlap=120,cmap='viridis');ax[0].set_title('start 5.19s, 80ms')
ax[1].plot(np.abs(x[::50]))
plt.savefig('z2.png',dpi=70)
