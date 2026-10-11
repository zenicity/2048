import numpy as np
y=np.load('yall.npy'); N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
T=int(8*499999.75)
L=(T//N)*N
for off in (0,32,64,96):
    Y=y[off:off+L-0].reshape(-1,N)[:-1]
    Fu=np.abs(np.fft.fft(Y*dn,axis=1)); Fd=np.abs(np.fft.fft(Y*up,axis=1))
    qu=Fu.max(1)/Fu.mean(1); qd=Fd.max(1)/Fd.mean(1)
    print(off,'frac windows q>8: dechirp-by-dn(upchirp sigs)',(qu>8).mean().round(3),' dechirp-by-up (downchirp sigs)',(qd>8).mean().round(3), 'baseline q noise ~',np.median(qu).round(2))
