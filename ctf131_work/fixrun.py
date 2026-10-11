import numpy as np, pickle, collections
from fix import *
def okc(by,ln=136):
    if len(by)<ln+2: return False
    c=crc16(by[:ln-2]); c^=by[ln-1]^(by[ln-2]<<8)
    return c==(by[ln]|by[ln+1]<<8)
res=pickle.load(open('res4.pkl','rb'))
cnt=collections.Counter(); out={}
for k,r in enumerate(res):
    if len(r['ds'])<205: continue
    fx,dec=decode_fixed(r['ds'])
    if dec is None: cnt[(r['pw']>20,'nolen')]+=1; continue
    hn,ln,cr,crc,by=dec
    o=okc(by,ln)
    cnt[(r['pw']>20,o)]+=1
    out[k]=(r['pw']>20,o,by)
print(sorted(cnt.items(),key=str))
pickle.dump(out,open('fixed.pkl','wb'))
