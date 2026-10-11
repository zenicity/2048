import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.signal import resample_poly
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8)
x=(d[0::2]+1j*d[1::2]).astype(np.complex64); del d
n=np.arange(len(x))
fc=-300.0e3
z=x*np.exp(-2j*np.pi*fc*(n%1999999)/fs).astype(np.complex64)
del x
y=resample_poly(z,1,500)   # 4 ksps
np.save('c300.npy',y); print(len(y), fs/500)
