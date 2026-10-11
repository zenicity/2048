import numpy as np, pickle, collections
from fix2 import *
res=pickle.load(open('res4.pkl','rb'))
def decode_trust(ds,k=3):
    d=list(ds)
    r=[int(round(v))%128 for v in d]
    fixed=list(r); good=[]
    for b in range(40):
        idx=range(8+5*b,13+5*b)
        if 12+5*b>=len(d): good.append(False); continue
        fb=fixblock([d[i] for i in idx],k)
        for i,v in zip(idx,fb): fixed[i]=v
        good.append(bad_rows(fb)==0)
    hn,ln2,cr,crc,by=decode(fixed)
    # nibble j belongs to block j//7 ; byte i = nibbles 2i,2i+1
    tr=np.zeros(len(by),bool)
    for i in range(len(by)):
        b1=(2*i)//7; b2=(2*i+1)//7
        tr[i]=(b1<len(good) and b2<len(good) and good[b1] and good[b2])
    return by,tr
F={}
for k,r in enumerate(res):
    if len(r['ds'])<205: continue
    by,tr=decode_trust(r['ds'])
    if len(by)>=136 and by[:2]==b'AL' and by[6]<=4 and by[7]<=127 :
        F.setdefault((('S' if r['pw']>20 else 'W'),by[6],by[7]),[]).append((np.frombuffer(by[8:136],dtype=np.uint8).astype(float),tr[8:136]))
pickle.dump(F,open('F.pkl','wb'))
print(len(F))
