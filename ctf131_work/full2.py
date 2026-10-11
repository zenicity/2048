import numpy as np, pickle, collections
exec(open('full.py').read().split("out=[]")[0])
def pll(ds,gain=0.15):
    c=0.0; r=[]
    for d in ds:
        s=int(np.round(d-c))
        e=(d-c)-s
        c+=gain*e
        r.append(s%128)
    return r
def decode2(ds,gain):
    r=pll(ds,gain)
    hs=[(((v-1)%128)>>2) for v in r[:8]]
    return None
def ok(by,ln=136):
    if len(by)<ln+2: return False
    c=crc16(by[:ln-2]); c^=by[ln-1]^(by[ln-2]<<8)
    return c==(by[ln]|by[ln+1]<<8)
import sys
def run(gain):
    cnt=collections.Counter()
    outp=[]
    for k,r in enumerate(res):
        if len(r['ds'])<205: continue
        rr=pll(r['ds'],gain) if gain>0 else [int(round(v))%128 for v in r['ds']]
        ds2=rr
        hn,ln,cr,crc,by=decode(ds2)
        o=ok(by,ln) if ln<=136 else False
        cnt[(r['pw']>20,o)]+=1
        outp.append((k,r['st']/499999.75,r['pw'],hn,by,o))
    return cnt,outp
for g in (0,0.05,0.1,0.2,0.3):
    c,_=run(g); print(g,sorted(c.items()))
