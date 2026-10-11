import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.signal import resample_poly
fs=1999999.0
T=6.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*T),offset=0)
x=(d[0::2]+1j*d[1::2]).astype(np.complex64)
n=np.arange(len(x))
for fc in (-290e3,):
    z=x*np.exp(-2j*np.pi*fc*n/fs).astype(np.complex64)
    y=resample_poly(z,1,100)  # 20 ksps
    fig,ax=plt.subplots(2,1,figsize=(14,10))
    ax[0].specgram(y,NFFT=512,Fs=fs/100,noverlap=256,cmap='viridis')
    ax[0].set_title(f'{fc/1e3} kHz, 20ksps')
    P=np.abs(np.fft.fftshift(np.fft.fft(y[:len(y)//8192*8192].reshape(-1,8192),axis=1),axes=1))**2
    ax[1].plot(np.fft.fftshift(np.fft.fftfreq(8192,100/fs)),10*np.log10(P.mean(0)))
    plt.savefig('nb.png',dpi=70)
