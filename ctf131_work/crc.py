import pickle, collections
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
res=[]
for k,t,pw,hn,by in out:
    res.append((k,t,pw>20,ok(by)))
print(collections.Counter((s,o) for _,_,s,o in res))
bad=[(k,round(t,2),s) for k,t,s,o in res if not o]
print(bad[:60])
