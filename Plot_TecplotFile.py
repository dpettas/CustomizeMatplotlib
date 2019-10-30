import numpy             as np
import binarytecplot     as bt
import my_mpl_template   as my_mpl
import matplotlib.pyplot as plt

from   my_mpl_template   import Blue, Red, Green,Black, Orange



# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Dependencies: 
# 				binarytecplot
# 				https://github.com/dpettas/ReadBinaryTecplotFiles
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


tecline   = bt.LoadTecplotFile("Rect.plt", info = True)


print()

zone      = tecline.getZone()
x         = zone["X"]
y         = zone["Y"]
z         = zone["Vx"]
triangles = zone.getConnectivity()




my_mpl.graph_mode('publication')

fig, gs   = my_mpl.figure()
ax0       = fig.add_subplot(gs[0,0])


vmax      =  10
vmin      = -10
lvs       = np.linspace(vmin,vmax, 11)


cb = ax0.tricontourf(x,y,triangles,zone["Txx"], cmap = "RdBu_r",
                     levels = lvs,
                     extend = 'both',
                     alpha  = 1.0)



speed = zone["Vx"]**2 + zone["Vy"]**2



stream_points = np.array([  
                             [0.10 , 0.05],
                             [0.01 , 0.14],
                             [0.10 , 0.10],
                             [0.26 ,-0.10],
                             [0.26 ,-0.15],
                             [0.40 ,-0.10],
                             [0.50 ,-0.10],
                             [0.50 ,-0.20],
                             [0.60 , 0.00],
                             [0.74 ,-0.19],
                             [0.30 ,-0.20],
                             [0.70 ,-0.20],
                           ])

# ax0.tricontourf(x,y,triangles,speed)
ax0.triplot   (x,y,triangles, color = Black[0].getColor(), linewidth = 0.3)
ax0.background(x,y,triangles, 0.4, cmap = 'Purples')

# ax0.tristreamplot(x, y,triangles, 
# 	              zone["Vx"],
# 	              zone["Vy"],
# 	              density      = 10.0,
# 	              color        = Black[0].getColor(),
# 	              linewidth    = 0.50 + 2.5 * np.tanh( 1.5 *  speed ), 
# 	              cmap         = "jet",
# 	              start_points = stream_points      )



# ax0.tristreamplot(x, y,triangles, 
# 	              zone["Vx"],
# 	              zone["Vy"],
# 	              density      = 10.0,
# 	              color        = zone["Psi"],
# 	              linewidth    = 0.25 + 2.0 * np.tanh( 1.5 *  speed ), 
# 	              cmap         = "RdBu_r",
# 	              start_points = stream_points )





ax0.plot(
	     [0.0, 0.25, 0.25, 0.75, 0.75, 1.00, 1.00, 0.00, 0.00], 
	     [0.0, 0.00,-0.25,-0.25, 0.00, 0.00,-0.50,-0.50, 0.00], color = "k", linewidth = 2.0)
ax0.fill(
	     [0.0, 0.25, 0.25, 0.75, 0.75, 1.00, 1.00, 0.00, 0.00], 
	     [0.0, 0.00,-0.25,-0.25, 0.00, 0.00,-0.50,-0.50, 0.00], color = "#DCDCDC", fill = True)

ax0.set_ylim( -0.30, 0.30)
ax0.set_xlim( -0.00, 1.00)

ax0.set_aspect(1.0)
ax0.axis('off')
plt.tight_layout()

plt.savefig("StreamPlot.png", dpi = 300)
plt.show()