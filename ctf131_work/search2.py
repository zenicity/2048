import numpy as np, pickle, collections
res=pickle.load(open('res4.pkl','rb'))
M=np.array([np.round(r['ds'][:200]).astype(int)%128 for r in res if len(r['ds'])>=200])
print(M.shape)
print(collections.Counter(M[:,0]).most_common(4),collections.Counter(M[:,3]).most_common(4))
for c in range(0,40):
    print(c,collections.Counter(M[:,c]).most_common(4), len(set(M[:,c])))
