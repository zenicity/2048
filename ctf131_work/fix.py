import numpy as np, pickle, itertools
exec(open('full.py').read().split("out=[]")[0])
def block_rows(symv):   # symv: list of 5 ints (raw bins incl +1 offset) -> codewords (7 five-bit)
    s=[((v-1)%128) for v in symv]; s=[v^(v>>1) for v in s]
    return deint(s,7,5)
def parity_bad(cws):
    return [bin(c).count('1')%2 for c in cws]
def decode_fixed(ds):
    d=np.array(ds,float)
    r=[int(round(v))%128 for v in d]
    alt=[(int(np.floor(v))%128 if v-np.floor(v)<0.5 else int(np.ceil(v))%128) for v in d]
    # alt = other neighbor of the measured value
    alt=[]
    for v in d:
        rr=int(round(v)); alt.append((rr+1 if v>rr else rr-1)%128)
    hn,ln,cr,crc,by=decode(r)
    if ln!=136: return r,None
    nblk=-(-2*(ln+2)//7)
    fixed=list(r)
    for b in range(nblk):
        idx=[8+5*b+i for i in range(5)]
        if idx[-1]>=len(fixed): break
        blk=[fixed[i] for i in idx]
        if sum(parity_bad(block_rows(blk)))==0: continue
        done=False
        # try single symbol alt
        for i in range(5):
            t=list(blk); t[i]=alt[idx[i]]
            if sum(parity_bad(block_rows(t)))==0:
                # choose the candidate with smallest |frac| distance (first found by confidence)
                pass
        cands=[]
        for i in range(5):
            t=list(blk); t[i]=alt[idx[i]]
            if sum(parity_bad(block_rows(t)))==0:
                cands.append((abs(d[idx[i]]-round(d[idx[i]])),i,t))
        if cands:
            cands.sort(key=lambda x:-x[0])   # most ambiguous symbol (frac nearest .5) is the culprit
            blk=cands[0][2]
            for i in range(5): fixed[idx[i]]=blk[i]
    return fixed,decode(fixed)
if __name__=='__main__':
    res=pickle.load(open('res4.pkl','rb'))
    import collections
    from full3 import ok
