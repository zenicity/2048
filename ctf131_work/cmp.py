import pickle, numpy as np
res=pickle.load(open('res4.pkl','rb'))
def sy(k): return np.round(res[k]['ds'][:208]).astype(int)%128
for (a,b) in [(1,2),(7,8),(13,14),(19,20),(25,26),(37,38)]:
    A,B=sy(a),sy(b)
    d=np.flatnonzero(A!=B)
    print(a,b,len(d),list(d), [(int(A[i]),int(B[i])) for i in d][:20])
