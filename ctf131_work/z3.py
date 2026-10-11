import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*0.25),offset=0)
x=d[0::2]+1j*d[1::2]
def seg(a,b): return x[int(a*fs):int(b*fs)]
fig,ax=plt.subplots(3,1,figsize=(14,13))
for a,b,l in [(0.01,0.045,'weak'),(0.125,0.178,'strong')]:
    s=seg(a,b); N=2048
    n=len(s)//N; P=np.abs(np.fft.fftshift(np.fft.fft(s[:n*N].reshape(n,N)*np.hanning(N),axis=1),axes=1))**2
    ax[0].plot(np.fft.fftshift(np.fft.fftfreq(N,1/fs))/1e3,10*np.log10(P.mean(0)),label=l)
ax[0].legend()
s=seg(0.12,0.135)
ax[1].specgram(s,NFFT=64,Fs=fs,noverlap=56,cmap='viridis',xextent=None); ax[1].set_title('strong 15ms')
s=seg(0.0,0.02)
ax[2].specgram(s,NFFT=64,Fs=fs,noverlap=56,cmap='viridis'); ax[2].set_title('weak')
plt.savefig('z3.png',dpi=70)
