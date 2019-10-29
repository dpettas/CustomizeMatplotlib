
import my_mpl_template          as     my_mpl
import matplotlib.pyplot        as     plt
from   my_mpl_template          import Blue, Red, Green,Black, Orange
from   my_mpl_template          import figure
from   my_mpl_template.FileData import FileData



# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Read Data
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

HEADER = "Re Ka El St A Hmax Hmin H1 H2"
F0 = FileData(filename = "./Data/El.0.00.dat", columns = HEADER)
F1 = FileData(filename = "./Data/El.0.25.dat", columns = HEADER)
F2 = FileData(filename = "./Data/El.0.50.dat", columns = HEADER)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Define graph mode either publication or presentation
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

my_mpl.graph_mode("publication")


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Define number of rows and columns 
# Note that each figure has size (6.4,4.8) inches 
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
fig, gs = figure(nrows = 1, ncols = 1)


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Define the Location of the graph on the grid
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

ax = []
ax.append( fig.add_subplot(gs[0,0])  )


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Plot the data
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


i = 0
ax[i].set_xlabel(r"$Re$")
ax[i].set_ylabel(r"$H_1$")
ax[i].plot(F0["Re"],F0["H1"], style = Blue  [0]  ,label = r"$El = 0.00$")
ax[i].plot(F1["Re"],F1["H1"], style = Red   [0]  ,label = r"$El = 0.25$")
ax[i].plot(F2["Re"],F2["H1"], style = Green [0]  ,label = r"$El = 0.50$")

ax[i].set_limit( xrange = (0.0, 20.0, 4.0, 0.50), 
	             yrange = (0.0, 6.0, 1.0, 0.25))

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

