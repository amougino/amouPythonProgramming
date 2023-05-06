
import numpy as np
import matplotlib.pyplot as plt


a = np.zeros( (100,100) )

x,y = np.meshgrid(np.arange(100),np.arange(100))

a= np.sqrt( (x-50)**2 + (y-50)**2 )
fig, ax = plt.subplots(2,2)
pm = ax[0,0].imshow(x)
fig.colorbar(pm,ax=ax[0,0])
ax[0,1].imshow(y)
ax[1,0].imshow(a)

b=a.copy()
b = np.where(a > 30, np.nan, b)
ax[1,1].imshow(b,vmin=0,vmax=np.max(a))

plt.show()

print('toto')
