import numpy as np
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8)
x=(d[0::2].astype(np.float32)+1j*d[1::2].astype(np.float32))
print(len(x)/fs)
N=4096
n=len(x)//N
X=x[:n*N].reshape(n,N)*np.hanning(N)
S=np.abs(np.fft.fftshift(np.fft.fft(X,axis=1),axes=1))**2
P=10*np.log10(S.mean(0)+1e-9)
f=np.fft.fftshift(np.fft.fftfreq(N,1/fs))
med=np.median(P)
print('median',med)
idx=np.argsort(P)[::-1][:40]
for i in sorted(idx): print(round(f[i]/1e3,1),round(P[i]-med,1))
# time activity per bin region
np.save('S.npy',S.astype(np.float32))
