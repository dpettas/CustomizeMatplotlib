import numpy             as np
import binarytecplot     as bt
import my_mpl_template   as my_mpl
import matplotlib.pyplot as plt

tecline   = bt.LoadTecplotFile("Rect.plt", info = True)

zone      = tecline.getZone()
x         = zone["X"]
y         = zone["Y"]
z         = zone["Vx"]
triangles = zone.getConnectivity()



fig, gs   = my_mpl.figure()
ax0       = fig.add_subplot(gs[0,0])


vmax      =  10
vmin      = -10
lvs       = np.linspace(vmin,vmax, 11)


cb = ax0.tricontourf(x,y,triangles,zone["Txx"], cmap = "RdBu_r",
                     levels = lvs,
                     extend = 'both',
                     alpha  = 1.0)


ax0.set_aspect(1.0)

plt.show()