import numpy as np, pickle
res=pickle.load(open('res4.pkl','rb'))
y=np.load('yall.npy'); N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
r=res[2]; a=r['a']
print(r['pw'],len(r['ds']))
q=[]
for i in range(0,230):
    s=y[a+i*N:a+(i+1)*N]
    if len(s)<N: break
    F=np.abs(np.fft.fft(s*dn)); G=np.abs(np.fft.fft(s*up))
    q.append((i,round(F.max()/F.mean(),1),round(G.max()/G.mean(),1)))
print(q)
