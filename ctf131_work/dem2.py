import numpy as np
y=np.load('y3.npy'); bw=1999999.0/4
SF=7;N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
def syms(st,count,off=0,c=dn):
    out=[]
    for i in range(count):
        s=y[st+off+i*N: st+off+(i+1)*N]
        if len(s)<N: break
        F=np.abs(np.fft.fft(s*c)); out.append((int(F.argmax()),F.max()/ (F.mean()+1e-9)))
    return out
st=int(0.0041*bw)
best=None
for off in range(N):
    r=syms(st,10,off)
    sc=sum(q for _,q in r)
    if best is None or sc>best[0]: best=(sc,off)
print(best)
off=best[1]
r=syms(st,200,off)
print([b for b,_ in r])
print([round(q) for _,q in r])
