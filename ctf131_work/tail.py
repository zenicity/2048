import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fs=1999999.0
# burst 32 at 2.0733 s, ends ~2.0733+0.0606
t0=2.0733+0.052; t1=2.0733+0.0640
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*(t1-t0)),offset=2*int(fs*t0))
x=d[0::2]+1j*d[1::2]
fig,ax=plt.subplots(2,1,figsize=(14,10))
ax[0].specgram(x,NFFT=256,Fs=fs,noverlap=224,cmap='viridis'); ax[0].set_title('tail of burst 32 (t from %.4f)'%t0)
ax[1].plot(np.abs(x[::20]))
plt.savefig('tail.png',dpi=65)
