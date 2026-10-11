import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.signal import resample_poly, firwin, lfilter
y=np.load('nb_p900.npy'); fs=1999999/200
# frequency of the line: PSD
N=1<<15
P=np.zeros(N)
for i in range(0,len(y)-N,N//2): P+=np.abs(np.fft.fft(y[i:i+N]*np.hanning(N)))**2
f=np.fft.fftfreq(N,1/fs); k=np.argmax(P*(np.abs(f)<2000)); print('peak freq offset Hz',f[k], 'P',10*np.log10(P[k]),'median',10*np.log10(np.median(P)))
fo=f[k]
n=np.arange(len(y))
z=y*np.exp(-2j*np.pi*fo*n/fs)
z=resample_poly(z,1,10)  # 1 kHz
fs2=fs/10
b=firwin(101,200,fs=fs2); z=lfilter(b,1,z)
env=np.abs(z)
np.save('env900.npy',env)
t=np.arange(len(env))/fs2
fig,ax=plt.subplots(2,1,figsize=(18,8))
ax[0].plot(t,env); ax[0].set_title('env +900k line, narrow')
m=(t>0)&(t<6)
ax[1].plot(t[m],env[m])
plt.savefig('env900.png',dpi=55)
print(np.percentile(env,[5,50,95,99]))
