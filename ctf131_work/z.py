import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*0.3),offset=2*int(fs*5))
x=d[0::2]+1j*d[1::2]
fig,ax=plt.subplots(2,1,figsize=(14,10))
ax[0].specgram(x,NFFT=256,Fs=fs,noverlap=192,cmap='viridis')
ax[0].set_title('0.3s @5s')
x2=x[:int(fs*0.03)]
ax[1].specgram(x2,NFFT=128,Fs=fs,noverlap=120,cmap='viridis')
plt.savefig('z.png',dpi=70)
