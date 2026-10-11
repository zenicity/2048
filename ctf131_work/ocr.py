import numpy as np, pickle, itertools, string
from PIL import Image, ImageDraw, ImageFont
T=pickle.load(open('T2.pkl','rb'))   # rows 80..119, 128 cols
f=ImageFont.load_default()
def render(s,x,y,W=128,H=40,grey=True):
    im=Image.new('L',(W,H),0); d=ImageDraw.Draw(im); d.text((x,y),s,font=f,fill=255)
    return np.array(im,float)/255
valid=~np.isnan(T)
Tz=np.where(valid,T,0)
def score(s,x,y,rows,cols):
    R=render(s,x,y)   # canvas rows 0..39 correspond to image rows 80..119
    r0,r1=rows[0]-80,rows[1]-80; c0,c1=cols
    Rr=R[r0:r1,c0:c1]; Tt=Tz[r0:r1,c0:c1]; V=valid[r0:r1,c0:c1]
    a=(Rr*V).ravel(); b=Tt.ravel()
    if a.std()<1e-6: return -1
    return np.corrcoef(a,b)[0,1]
# calibrate on line 1
best=None
for x in range(48,60):
    for y in range(78,92):
        sc=score('GAIANSPACE{',x,y-80+80-0,(82,95),(48,124))
        # y here is canvas y (0..39) so convert: image row = 80+canvas y => canvas y = rowoffset
        pass
best=None
for x in range(46,60):
    for cy in range(0,12):
        sc=score('GAIANSPACE{',x,cy+80-80+0,(82,95),(46,124)) if False else None
