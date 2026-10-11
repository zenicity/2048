import numpy as np, pickle, collections
exec(open('full_b.py').read().split("out=[]")[0])
def ok(by,ln=136):
    if len(by)<ln+2: return False
    c=crc16(by[:ln-2]); c^=by[ln-1]^(by[ln-2]<<8)
    return c==(by[ln]|by[ln+1]<<8)
def circmed(fr):
    return np.median(fr)
out=[]
cnt=collections.Counter()
for k,r in enumerate(res):
    if len(r['ds'])<205: continue
    d=np.array(r['ds'])
    best=None
    for o in (0,-1,1,-2,2):
        for fr_mode in (0,1):
            if fr_mode:
                fr=d-np.round(d); c0=np.median(fr)
                rr=[int(np.round(v-c0))%128 for v in d]
            else:
                rr=[int(np.round(v))%128 for v in d]
            rr=[(v+o)%128 for v in rr]
            hn,ln,cr,crc,by=decode(rr)
            if ln<=136 and ok(by,ln): best=(o,fr_mode,hn,by); break
        if best: break
    cnt[(r['pw']>20,bool(best))]+=1
    if best: out.append((k,r['st']/499999.75,r['pw'],best[2],best[3],best[0]))
print(sorted(cnt.items()))
pickle.dump(out,open('good.pkl','wb'))
print(collections.Counter(o[5] for o in out))
