import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.signal import resample_poly
fs=1999999.0
a,b=0.060,0.085  # weak burst (0.0573 start)
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*(b-a)),offset=2*int(fs*a))
x=(d[0::2]+1j*d[1::2]).astype(np.complex64)
n=np.arange(len(x))
fig,ax=plt.subplots(3,1,figsize=(14,13))
for i,fc in enumerate((-425e3,-330e3)):
    z=x*np.exp(-2j*np.pi*fc*n/fs).astype(np.complex64)
    y=resample_poly(z,1,8) # 250k
    ax[i].specgram(y,NFFT=128,Fs=fs/8,noverlap=112,cmap='viridis')
    ax[i].set_title(f'center {fc/1e3} kHz, 250ksps (weak burst)')
ax[2].specgram(x,NFFT=128,Fs=fs,noverlap=112,cmap='viridis')
plt.savefig('hump.png',dpi=65)
