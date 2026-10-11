import numpy as np
from scipy.signal import resample_poly
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8,count=2*int(fs*3),offset=0)
x=(d[0::2]+1j*d[1::2]).astype(np.complex64)
# decimate by 4
y=resample_poly(x,1,4)
np.save('y3.npy',y)
bw=fs/4
def chirp(SF,up=True):
    N=2**SF
    n=np.arange(N)
    ph=np.pi*(n*n/N - n)   # k=1 upchirp from -bw/2: phase = pi*(n^2/N - n)
    c=np.exp(1j*ph)
    return c if up else np.conj(c)
for SF in (5,6,7,8,9):
    N=2**SF; dc=chirp(SF,False)
    # burst1: samples from 0.0041s
    st=int(0.0041*bw); seg=y[st:st+int(0.045*bw)]
    best=[]
    for off in range(0,N,max(1,N//32)):
        n=(len(seg)-off)//N
        blocks=seg[off:off+n*N].reshape(n,N)*dc
        F=np.abs(np.fft.fft(blocks,axis=1))
        best.append((F.max(1).mean()/F.mean(),off))
    print(SF,max(best))
