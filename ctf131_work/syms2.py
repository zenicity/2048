import numpy as np, pickle
y=np.load('yall.npy')
N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
Z=8
out=pickle.load(open('bursts.pkl','rb'))
def fb(s,c):
    F=np.abs(np.fft.fft(s*c,N*Z)); k=int(F.argmax())
    # parabolic
    a,b,cc=F[(k-1)%(N*Z)],F[k],F[(k+1)%(N*Z)]
    d=0.5*(a-cc)/(a-2*b+cc+1e-12)
    return ((k+d)/Z)%N
res=[]
for st,en,a0,pw,_ in out:
    best=None
    for off in range(-N//2,N//2):
        a=a0+off
        sc=sum(np.abs(np.fft.fft(y[a+i*N:a+(i+1)*N]*dn)).max() for i in range(6))
        if best is None or sc>best[0]: best=(sc,a)
    a=best[1]
    pre=[fb(y[a+i*N:a+(i+1)*N],dn) for i in range(8)]
    sync=[fb(y[a+i*N:a+(i+1)*N],dn) for i in (8,9)]
    sfd=[fb(y[a+i*N:a+(i+1)*N],up) for i in (10,11)]
    d0=a+int(12.25*N)
    ds=[]
    i=0
    while d0+(i+1)*N<=len(y) and d0+(i+1)*N<=en+N//2 and i<260:
        ds.append(fb(y[d0+i*N:d0+(i+1)*N],dn)); i+=1
    res.append(dict(st=st,en=en,a=a,pw=pw,pre=pre,sync=sync,sfd=sfd,ds=ds))
pickle.dump(res,open('res2.pkl','wb'))
for r in res[:6]:
    print(round(r['pw']),np.round(np.mean(r['pre']),2),np.round(np.std(r['pre']),2),np.round(r['sync'],2),np.round(r['sfd'],2),len(r['ds']),np.round(r['ds'][:10],2))
