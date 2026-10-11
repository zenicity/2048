import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.signal import resample_poly
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8)
x=(d[0::2]+1j*d[1::2]).astype(np.complex64); del d
n=np.arange(len(x))
out={}
for name,fc in (('p900',900e3),('m290',-290e3)):
    z=x*np.exp(-2j*np.pi*fc*(n%int(fs))/fs).astype(np.complex64)  # keep phase approx
    y=resample_poly(z,1,200)  # 10 ksps
    out[name]=y
    np.save(f'nb_{name}.npy',y)
    print(name,len(y))
