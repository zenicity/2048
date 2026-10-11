import numpy as np, pickle, collections
allr=pickle.load(open('allr.pkl','rb'))
M=np.array([r[1][:200] for r in allr])
print(M.shape)
# per column distinct counts
for c in range(0,200,1):
    cnt=collections.Counter(M[:,c]); top=cnt.most_common(3)
    print(c,len(cnt),top)
