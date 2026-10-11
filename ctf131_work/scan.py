import numpy as np, pickle
y=np.load('yall.npy'); bw=1999999.0/4
N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
k=32
p=np.abs(y)**2
sm=np.convolve(p,np.ones(k)/k,'same')
noise=np.percentile(sm,3)
print('noise',10*np.log10(noise), [10*np.log10(np.percentile(sm,q)) for q in (3,10,20,50,80,95)])
thr=noise*6
on=sm>thr
e=np.flatnonzero(np.diff(on.astype(np.int8)))
starts=[i+1 for i in e if not on[i]]
ends=[i for i in e if on[i]]
if on[0]: ends=ends[1:]
bursts=[(s,en) for s,en in zip(starts,ends) if en-s>20000]
print(len(bursts))
def sym(s,c=dn):
    F=np.abs(np.fft.fft(s*c)); return int(F.argmax()),F.max()/F.mean()
out=[]
for st,en in bursts:
    best=None
    for off in range(-N,N,2):
        a=st+off
        if a<0: continue
        sc=sum(sym(y[a+i*N:a+(i+1)*N])[1] for i in range(4))
        if best is None or sc>best[0]: best=(sc,a)
    a=best[1]
    syms=[sym(y[a+i*N:a+(i+1)*N])[0] for i in range(12)]
    pw=10*np.log10(sm[st+2000])
    out.append((st,en,a,pw,syms))
pickle.dump(out,open('bursts.pkl','wb'))
for st,en,a,pw,s in out[:60]: print(f"{st/bw:.4f} {(en-st)/bw*1000:.1f}ms pw={pw:.0f} a={a-st}",s)
