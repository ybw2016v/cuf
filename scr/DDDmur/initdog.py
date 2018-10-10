#!/usr/bin/env python3
import numpy as np
a=np.ones([256,256,80],dtype='float32')
a[80:120,90:100,20:70]=0
np.save('dogz',a)