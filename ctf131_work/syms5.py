import numpy as np, pickle
exec(open('syms3.py').read().split("res=[]")[0])
res=[]
for st,en,a0,pw,_ in out:
    a=st
    for it in range(3):
        pu=np.mean([fb(y[a+i*N:a+(i+1)*N],dn) for i in range(2,7)])
        pd=np.mean([fb(y[a+i*N:a+(i+1)*N],up) for i in (10,11)])
        a=a+int(round(-wrap(pu-pd)/2))
    pu=np.mean([fb(y[a+i*N:a+(i+1)*N],dn) for i in range(2,7)])
    pd=np.mean([fb(y[a+i*N:a+(i+1)*N],up) for i in (10,11)])
    cfo=wrap(pu)
    d0=a+int(12.25*N)
    ds=[]
    i=0
    while d0+(i+1)*N<=len(y) and d0+i*N<en-N//2 and i<300:
        ds.append(wrap(fb(y[d0+i*N:d0+(i+1)*N],dn)-cfo)); i+=1
    res.append(dict(st=st,en=en,a=a,pw=pw,cfo=cfo,ds=np.array(ds)))
pickle.dump(res,open('res5.pkl','wb'))
for r in res[:6]: print(len(r['ds']),np.round(r['ds'][:24],1))
