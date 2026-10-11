import numpy as np
fs=1999999.0
S=np.load('S.npy')  # rows of 4096 samples (2.048ms), 4096 bins fftshift
f=np.fft.fftshift(np.fft.fftfreq(4096,1/fs))
def band(lo,hi): return S[:,(f>=lo)&(f<hi)].sum(1)
tot=10*np.log10(S.sum(1)+1)
inner=10*np.log10(band(-200,200)+1)
outer=10*np.log10(band(300,550)+1)
t=np.arange(len(tot))*4096/fs
# print coarse
for i in range(0,len(tot),1):
    if t[i]<1.0: print(f"{t[i]:.4f} tot={tot[i]:.1f} in={inner[i]:.1f} out={outer[i]:.1f}")
