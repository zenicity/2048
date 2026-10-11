import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*0.12),offset=0)
x=d[0::2]+1j*d[1::2]
fig,ax=plt.subplots(2,1,figsize=(14,10))
a,b=0.0465,0.0585
s=x[int(a*fs):int(b*fs)]
ax[0].specgram(s,NFFT=256,Fs=fs,noverlap=224,cmap='viridis');ax[0].set_title('gap region')
a,b=0.1147,0.1235
s=x[int(a*fs):int(b*fs)]
ax[1].specgram(s,NFFT=256,Fs=fs,noverlap=224,cmap='viridis')
plt.savefig('z4.png',dpi=70)
