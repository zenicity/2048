import numpy as np
from scipy.signal import resample_poly
fs=1999999.0
d=np.fromfile('cap.sigmf-data',dtype=np.int8)
x=(d[0::2]+1j*d[1::2]).astype(np.complex64)
del d
y=resample_poly(x,1,4).astype(np.complex64)
np.save('yall.npy',y)
print(len(y))
