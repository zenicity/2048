import itertools
H=[33,13,1,45,125,105,89,85]
def ig(x):
    r=x
    while x>>1: x>>=1; r^=x
    return r
for delta in (0,1,2):
  for rnd in (0,):
    s=[((v-delta)%128)>>2 for v in H]
    for gm in (0,1,2):
      g=[v if gm==0 else (v^(v>>1) if gm==1 else ig(v)) for v in s]
      for c in (-1,0,1,2):
        for rev in (0,1):
          inter=[[(v>>(4-j))&1 for j in range(5)] for v in g]
          if rev: inter=[l[::-1] for l in inter]
          de=[[0]*8 for _ in range(5)]
          for i in range(8):
            for j in range(5):
              de[(i-j-c)%5][i]=inter[i][j]
          cws=[int(''.join(map(str,r)),2) for r in de]
          for order in ('top','bot'):
            nib=[(cw>>4 if order=='top' else cw&15) for cw in cws]
            print(delta,gm,c,rev,order,[f"{x:x}" for x in nib],[f"{cw:08b}" for cw in cws])
