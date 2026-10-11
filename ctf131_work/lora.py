import numpy as np, pickle
y=np.load('yall.npy'); bw=1999999.0/4
SF=7;N=128
n=np.arange(N); up=np.exp(1j*np.pi*(n*n/N-n)); dn=np.conj(up)
def wh(nb):
    s=0xFF;o=[]
    for _ in range(nb):
        o.append(s); b=((s>>7)^(s>>5)^(s>>4)^(s>>3))&1; s=((s<<1)&0xFF)|b
    return o
WH=wh(300)
def igray(x):
    r=x
    while x>>1: x>>=1; r^=x
    return r
def getsyms(a,pre,nsym):
    d0=a+int(12.25*N)
    out=[]
    for i in range(nsym):
        s=y[d0+i*N:d0+(i+1)*N]
        if len(s)<N: break
        F=np.abs(np.fft.fft(s*dn)); out.append(int(F.argmax()))
    return out
def hamming(cw,cwlen):
    # cw int with cwlen bits, MSB-first positions; data = top 4 bits
    return cw>>(cwlen-4)
def deint(symbols,sf_app,cwlen,gray):
    # symbols: list of cwlen ints each sf_app bits
    inter=[[ (s>>(sf_app-1-j))&1 for j in range(sf_app)] for s in symbols]
    de=[[0]*cwlen for _ in range(sf_app)]
    for i in range(cwlen):
        for j in range(sf_app):
            de[(i-j-1)%sf_app][i]=inter[i][j]
    cws=[]
    for r in de:
        v=0
        for b in r: v=(v<<1)|b
        cws.append(v)
    return cws
def decode(a,pre,delta=0,gray=1,verbose=True):
    r=getsyms(a,pre,300)
    r=[(v-pre)%N for v in r]
    hdr=r[:8]
    res={}
    s=[(( (v-delta)%N)>>2) for v in hdr]
    s=[ (igray(v) if gray==1 else (v^(v>>1)) ) for v in s]
    cws=deint(s,5,8,gray)
    nib=[hamming(c,8) for c in cws]
    return r,nib
if __name__=='__main__':
    out=pickle.load(open('bursts.pkl','rb'))
    for k in (0,2,3):
        st,en,a,pw,syms=out[k]; pre=syms[0]
        for delta in (0,1,-1):
            for gray in (0,1):
                r,nib=decode(a,pre,delta,gray)
                print(k,delta,gray,[hex(v) for v in nib])
