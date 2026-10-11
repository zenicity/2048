import numpy as np
y=np.load('y3.npy'); bw=1999999.0/4
SF=7;N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
p=np.abs(y)**2
k=32
sm=np.convolve(p,np.ones(k)/k,'same')
noise=np.median(sm[sm<np.percentile(sm,30)])
thr=noise*8
on=sm>thr
edges=np.flatnonzero(np.diff(on.astype(int)))
starts=edges[::2] if on[0]==False else edges[1::2]
starts=[e+1 for e in edges if not on[e]]
ends=[e for e in edges if on[e]]
print(len(starts),len(ends))
def sym(s,c=dn):
    F=np.abs(np.fft.fft(s*c)); return int(F.argmax()),F.max()/F.mean()
res=[]
for st,en in list(zip(starts,ends))[:40]:
    if en<st: continue
    best=None
    for off in range(-N,N,2):
        a=st+off
        if a<0: continue
        sc=sum(sym(y[a+i*N:a+(i+1)*N])[1] for i in range(4))
        if best is None or sc>best[0]: best=(sc,a)
    a=best[1]
    syms=[sym(y[a+i*N:a+(i+1)*N]) for i in range(14)]
    print(f"{st/bw:.4f} len={(en-st)/bw*1000:.1f}ms pw={10*np.log10(sm[st+500]):.0f}", [b for b,_ in syms][:12], [round(q) for _,q in syms][:12])
