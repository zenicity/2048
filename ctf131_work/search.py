import numpy as np, pickle, collections, itertools
allr=pickle.load(open('allr.pkl','rb'))
M=np.array([r[1][:200] for r in allr])
def igray(x):
    r=x
    while x>>1: x>>=1; r^=x
    return r
def run(delta,gm,c,cw,sf=7,start=8,nblocks=3,rev=False):
    cnt=collections.Counter()
    for row in M:
        for b in range(nblocks):
            sy=row[start+b*cw:start+(b+1)*cw]
            s=[((v-delta)%128) for v in sy]
            if gm==1: s=[v^(v>>1) for v in s]
            elif gm==2: s=[igray(v) for v in s]
            inter=[[ (v>>(sf-1-j))&1 for j in range(sf)] for v in s]
            if rev: inter=[l[::-1] for l in inter]
            de=[[0]*cw for _ in range(sf)]
            for i in range(cw):
                for j in range(sf):
                    de[(i-j-c)%sf][i]=inter[i][j]
            for r in de:
                v=0
                for bt in r: v=(v<<1)|bt
                cnt[v]+=1
    return len(cnt), cnt
res=[]
for delta in (0,1,2):
  for gm in (0,1,2):
    for c in range(-2,3):
      for rev in (False,True):
        for cw in (5,6,7,8):
            n,_=run(delta,gm,c,cw,rev=rev)
            res.append((n/2**cw,n,delta,gm,c,rev,cw))
res.sort()
for r in res[:15]: print(r)
