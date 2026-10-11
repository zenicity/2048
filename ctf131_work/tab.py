import pickle, collections
out=pickle.load(open('pk.pkl','rb'))
print(len(out))
for k,t,pw,hn,by in out[:60]:
    print(k,f"{t:.3f}",'S' if pw>20 else 'w',by[:8].hex(),by[8:16].hex(), len(by), by[-6:].hex())
print(collections.Counter(by[:2] for *_,by in out))
print(collections.Counter(by[2:6].hex() for *_,by in out).most_common(10))
