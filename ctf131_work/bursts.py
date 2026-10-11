import numpy as np
fs=1999999.0
S=np.load('S.npy'); tot=10*np.log10(S.sum(1)+1)
dt=4096/fs
lvl=np.where(tot>95,2,np.where(tot>66,1,0))
segs=[];s=0
for i in range(1,len(lvl)+1):
    if i==len(lvl) or lvl[i]!=lvl[s]:
        segs.append((lvl[s],s*dt,(i-s)*dt)); s=i
print(len(segs))
for k,(l,t,d) in enumerate(segs[:80]): print(k,l,f"{t:.4f} {d*1000:.1f}ms")
import collections
print(collections.Counter(l for l,_,_ in segs))
