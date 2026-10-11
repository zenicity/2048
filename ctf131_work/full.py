import numpy as np, pickle
res=pickle.load(open('res4.pkl','rb'))
WH=[0xFF,0xFE,0xFC,0xF8,0xF0,0xE1,0xC2,0x85,0x0B,0x17,0x2F,0x5E,0xBC,0x78,0xF1,0xE3]
s=0xFF;WH=[]
for _ in range(300):
    WH.append(s); b=((s>>7)^(s>>5)^(s>>4)^(s>>3))&1; s=((s<<1)&0xFF)|b
def deint(symbols,sf_app,cw):
    inter=[[(v>>(sf_app-1-j))&1 for j in range(sf_app)] for v in symbols]
    de=[[0]*cw for _ in range(sf_app)]
    for i in range(cw):
        for j in range(sf_app): de[(i-j-1)%sf_app][i]=inter[i][j]
    return [int(''.join(map(str,r)),2) for r in de]
def nib(c,cw): # reversed top4
    bits=[(c>>(cw-1-k))&1 for k in range(cw)]
    return bits[3]<<3|bits[2]<<2|bits[1]<<1|bits[0]
def crc16(data,init=0):
    crc=init
    for b in data:
        crc^=b<<8
        for _ in range(8):
            crc=((crc<<1)^0x1021)&0xFFFF if crc&0x8000 else (crc<<1)&0xFFFF
    return crc
def decode(ds):
    r=[int(round(v))%128 for v in ds]
    hs=[(((v-1)%128)>>2) for v in r[:8]]
    hs=[v^(v>>1) for v in hs]
    cws=deint(hs,5,8)
    hn=[nib(c,8) for c in cws]
    ln=hn[0]<<4|hn[1]; cr=hn[2]>>1; crc=hn[2]&1
    cwl=cr+4
    nn=2*(ln+2*crc)
    nblk=-(-nn//7)
    sy=[(((v-1)%128)) for v in r[8:8+nblk*cwl]]
    sy=[v^(v>>1) for v in sy]
    nibs=[]
    for b in range(nblk):
        blk=sy[b*cwl:(b+1)*cwl]
        if len(blk)<cwl: break
        nibs+= [nib(c,cwl) for c in deint(blk,7,cwl)]
    by=[]
    for i in range(0,len(nibs)-1,2):
        o=i//2
        lo,hi=nibs[i],nibs[i+1]
        if o<ln: by.append(((hi<<4|lo)^WH[o]))
        else: by.append(hi<<4|lo)
    return hn,ln,cr,crc,bytes(by)
out=[]
for k,r in enumerate(res):
    if len(r['ds'])<205: continue
    hn,ln,cr,crc,by=decode(r['ds'])
    out.append((k,r['st']/499999.75,r['pw'],hn,by))
pickle.dump(out,open('pk.pkl','wb'))
for k,t,pw,hn,by in out[:8]:
    print(k,round(t,3),round(pw),hn,by[:ln_ if (ln_:=136) else 0])
