import numpy as np, pickle, itertools, collections
exec(open('full.py').read().split("out=[]")[0])
def okc(by,ln=136):
    if len(by)<ln+2: return False
    c=crc16(by[:ln-2]); c^=by[ln-1]^(by[ln-2]<<8)
    return c==(by[ln]|by[ln+1]<<8)
def bad_rows(blk):
    s=[((v-1)%128) for v in blk]; s=[v^(v>>1) for v in s]
    return sum(bin(c).count('1')%2 for c in deint(s,7,5))
def cands(v,k):
    rr=int(round(v)); fr=v-rr
    c=[rr,(rr+1 if fr>0 else rr-1),(rr-1 if fr>0 else rr+1)]
    return [x%128 for x in c[:k]]
def fixblock(vs,k=2):
    base=[int(round(v))%128 for v in vs]
    if bad_rows(base)==0: return base
    best=None
    for combo in itertools.product(*[cands(v,k) for v in vs]):
        if bad_rows(list(combo))==0:
            cost=sum(abs((c-v+64)%128-64)**2 for c,v in zip(combo,vs))
            if best is None or cost<best[0]: best=(cost,list(combo))
    return best[1] if best else base
def decode_full(ds,k=2):
    d=list(ds)
    r=[int(round(v))%128 for v in d]
    hn,ln,cr,crc,by=decode(r)
    ln=136
    nblk=-(-2*(ln+2)//7)   # 40
    fixed=list(r)
    for b in range(nblk):
        idx=range(8+5*b,13+5*b)
        if 12+5*b>=len(d): break
        fb=fixblock([d[i] for i in idx],k)
        for i,v in zip(idx,fb): fixed[i]=v
    hn,ln2,cr,crc,by=decode(fixed)
    return by
if __name__=='__main__':
    res=pickle.load(open('res4.pkl','rb'))
    for k in (2,3):
        cnt=collections.Counter(); out={}
        for kk,r in enumerate(res):
            if len(r['ds'])<205: continue
            by=decode_full(r['ds'],k)
            o=okc(by,136)
            cnt[(r['pw']>20,o)]+=1
            out[kk]=(r['pw']>20,o,by)
        print(k,sorted(cnt.items(),key=str))
        pickle.dump(out,open(f'fixed{k}.pkl','wb'))
