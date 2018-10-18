import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import imageio

End=20
outfilename = "test.gif"
frames=[]

for name in range(0,End+1):
    dogname='./res/p0_'+str(name)+'.npy'
    a=np.load(dogname)
    plt.imshow(a)
    plt.colorbar()
    plt.savefig(dogname+'.jpg')
    plt.close()
    
    frames.append(imageio.imread(dogname+'.jpg'))
    imageio.mimsave(outfilename, frames,'GIF', duration=0.5) 
    pass