import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.signal import resample_poly
fs=1999999.0
T=10.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*T),offset=0)
x=(d[0::2]+1j*d[1::2]).astype(np.complex64)
n=np.arange(len(x))
# fine PSD to locate narrow lines over whole 10 s
N=1<<16
P=np.zeros(N)
for i in range(0,len(x)-N,N*4):
    P+=np.abs(np.fft.fft(x[i:i+N]*np.hanning(N)))**2
P=np.fft.fftshift(P); f=np.fft.fftshift(np.fft.fftfreq(N,1/fs))
Pd=10*np.log10(P+1)
# local peak vs neighbors
from scipy.ndimage import median_filter
base=median_filter(Pd,size=401)
ex=Pd-base
idx=np.argsort(ex)[::-1][:25]
for i in sorted(idx): print(round(f[i]/1e3,2),round(ex[i],1))
