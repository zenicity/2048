import pickle, numpy as np, collections
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
out=pickle.load(open('pk.pkl','rb'))
def crc16(data):
    crc=0
    for b in data:
        crc^=b<<8
        for _ in range(8):
            crc=((crc<<1)^0x1021)&0xFFFF if crc&0x8000 else (crc<<1)&0xFFFF
    return crc
def ok(by,ln=136):
    if len(by)<ln+2: return False
    c=crc16(by[:ln-2]); c^=by[ln-1]^(by[ln-2]<<8)
    return c==(by[ln]|by[ln+1]<<8)
G={}
for k,t,pw,hn,by in out:
    if len(by)<138 or by[:2]!=b'AL': continue
    s,g=by[6],by[7]
    G.setdefault((g,s),[]).append((pw>20,ok(by),by[8:136]))
gs=sorted(set(g for g,s in G)); print(len(gs),gs[:5],gs[-5:], max(s for g,s in G))
fig,ax=plt.subplots(1,5,figsize=(20,12))
for s in range(5):
    img=np.zeros((max(gs)+1,128))
    for g in gs:
        L=G.get((g,s))
        if not L: continue
        good=[x for x in L if x[1]] or L
        img[g]=np.frombuffer(good[0][2],dtype=np.uint8)
    ax[s].imshow(img,aspect='auto',cmap='gray'); ax[s].set_title(f'slice {s}')
plt.savefig('img.png',dpi=60)
