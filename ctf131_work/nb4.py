import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(2,2,figsize=(18,10))
for j,name in enumerate(('p900','m290')):
    y=np.load(f'nb_{name}.npy'); fs=1999999/200
    ax[0,j].specgram(y[:int(fs*50)],NFFT=2048,Fs=fs,noverlap=1024,cmap='viridis'); ax[0,j].set_title(name+' full')
    ax[1,j].plot(np.abs(y[:int(fs*3)])); ax[1,j].set_title('env 0-3s')
plt.savefig('nb4.png',dpi=55)
