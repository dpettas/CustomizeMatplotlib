
import my_mpl_template          as     my_mpl
import matplotlib.pyplot        as     plt
from   my_mpl_template          import Blue, Red, Green,Black, Orange
from   my_mpl_template          import figure
from   my_mpl_template.FileData import FileData

import sys 

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Read Data
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

HEADER = "Re Ka El St A Hmax Hmin H1 H2"
F0 = FileData(filename = "./Data/El.0.00.dat", columns = HEADER)
F1 = FileData(filename = "./Data/El.0.25.dat", columns = HEADER)
F2 = FileData(filename = "./Data/El.0.50.dat", columns = HEADER)



for r in F0:
    print(r["Re"], r["H1"])


sys.exit(-1)
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Define graph mode either publication or presentation
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

my_mpl.graph_mode("publication")


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Define number of rows and columns 
# Note that each figure has size (6.4,4.8) inches 
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
fig, gs = figure(nrows = 1, ncols = 2)


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Define the Location of the graph on the grid
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

ax = []
ax.append( fig.add_subplot(gs[0,0])  )
ax.append( fig.add_subplot(gs[0,1])  )


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Plot the data
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


i = 0

ax[i].increase(portion = 10.0)
ax[i].set_xlabel(r"$Re$")
ax[i].set_ylabel(r"$H_1$")
ax[i].plot(F0["Re"],F0["H1"], style = Blue  [0]  ,label = r"$El = 0.00$")
ax[i].plot(F1["Re"],F1["H1"], style = Red   [0]  ,label = r"$El = 0.25$")
ax[i].plot(F2["Re"],F2["H1"], style = Green [0]  ,label = r"$El = 0.50$")

ax[i].set_limit( xrange = (0.0, 20.0, 4.0, 0.50), 
	             yrange = (0.0, 6.0, 1.0, 0.25))

ax[i].legend()
ax[i].subscript()

i = 1
ax[i].set_xlabel(r"$Re$")
ax[i].set_ylabel(r"$H_2$")
ax[i].plot(F0["Re"],F0["H2"], style = Blue  [0]  ,label = r"$El = 0.00$")
ax[i].plot(F1["Re"],F1["H2"], style = Red   [0]  ,label = r"$El = 0.25$")
ax[i].plot(F2["Re"],F2["H2"], style = Green [0]  ,label = r"$El = 0.50$")

ax[i].set_limit( xrange = (0.0, 20.0, 4.0, 0.50), 
	             yrange = (0.0, 16.0, 1.0, 0.25))

ax[i].legend()
ax[i].subscript()



# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Save the figure
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


plt.savefig("Test.png", dpi = 300)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Plot the figure
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

plt.show()

