import numpy as np, pickle, collections
res=pickle.load(open('res4.pkl','rb'))
M=np.array([np.round(r['ds'][:200]).astype(int)%128 for r in res if len(r['ds'])>=200])
mode=[collections.Counter(M[:,c]).most_common(1)[0][0] for c in range(40)]
print(mode[:24])
for delta in (0,1):
  for c in (0,1,2):
    for cw in (8,5,6,7):
      sy=mode[8:8+cw]
      s=[((v-delta)%128) for v in sy]
      s=[v^(v>>1) for v in s]
      inter=[[(v>>(6-j))&1 for j in range(7)] for v in s]
      de=[[0]*cw for _ in range(7)]
      for i in range(cw):
        for j in range(7): de[(i-j-c)%7][i]=inter[i][j]
      print(delta,c,cw,[''.join(map(str,r)) for r in de])
