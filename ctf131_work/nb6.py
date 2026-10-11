import numpy as np
from scipy.signal import resample_poly, firwin, lfilter
fs=1999999.0
y=np.load('nb_m290.npy'); fs1=fs/200   # 10 ksps, centered -290 kHz
# PSD of this narrow region restricted to gap-ish times? just overall
N=1<<15
P=np.zeros(N); cnt=0
for i in range(0,len(y)-N,N//2):
    P+=np.abs(np.fft.fft(y[i:i+N]*np.hanning(N)))**2; cnt+=1
f=np.fft.fftfreq(N,1/fs1)
m=np.abs(f)<3000
k=np.argmax(P*m); print('peak',f[k],10*np.log10(P[k]),'median',10*np.log10(np.median(P[m])))
top=np.argsort(P*m)[::-1][:10]; print([(round(f[i],1),round(10*np.log10(P[i]),1)) for i in top])
