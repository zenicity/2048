import numpy as np, pickle
y=np.load('yall.npy')
N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
Z=8
out=pickle.load(open('bursts.pkl','rb'))
def fb(s,c):
    F=np.abs(np.fft.fft(s*c,N*Z)); k=int(F.argmax())
    a,b,cc=F[(k-1)%(N*Z)],F[k],F[(k+1)%(N*Z)]
    d=0.5*(a-cc)/(a-2*b+cc+1e-12)
    return ((k+d)/Z)%N
def wrap(v): return (v+N/2)%N-N/2
res=[]
for st,en,a0,pw,_ in out:
    a=st
    for it in range(4):
        pu=np.mean([fb(y[a+i*N:a+(i+1)*N],dn) for i in range(2,7)])
        pd=np.mean([fb(y[a+i*N:a+(i+1)*N],up) for i in (10,11)])
        # downchirps at 10,11 exist only if a aligned within 1 symbol; use first guess
        t=wrap(pu-pd)/2
        a=a+int(round(-t)) if it<3 else a
    pu=np.mean([fb(y[a+i*N:a+(i+1)*N],dn) for i in range(2,7)])
    pd=np.mean([fb(y[a+i*N:a+(i+1)*N],up) for i in (10,11)])
    res.append((st,a,pu,pd,pw))
for r in res[:12]: print(r[0],r[1]-r[0],round(r[2],2),round(r[3],2),round(r[4]))
