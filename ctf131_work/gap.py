import numpy as np
fs=1999999.0
S=np.load('S.npy')  # (rows,4096) 2.048ms frames
f=np.fft.fftshift(np.fft.fftfreq(4096,1/fs))/1e3
tot=10*np.log10(S.sum(1)+1)
gap=S[tot<60]; act=S[(tot>70)&(tot<90)]
print(len(gap),len(act))
Pg=10*np.log10(gap.mean(0)+1); Pa=10*np.log10(act.mean(0)+1)
for lo in range(-1000,1000,50):
    m=(f>=lo)&(f<lo+50)
    print(lo,round(Pg[m].mean(),1),round(Pa[m].mean(),1))
