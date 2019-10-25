


from   FileData import FileData
import LineStyle         as LS 
import MyTemplates       as tmp 
import matplotlib.pyplot as plt


HEADER = "Re Ka El St A Hmax Hmin H1 H2"

F0 = FileData(filename = "./Data/El.0.00.dat", columns = HEADER)
F1 = FileData(filename = "./Data/El.0.25.dat", columns = HEADER)

fig, gs = tmp.figure(nrows = 1, ncols = 1)


ax = []
ax.append( fig.add_subplot(gs[0,0], projection = 'publication'  ))
# ax.append( fig.add_subplot(gs[0,1], projection = 'publication'  ))



ii = 0
ax[ii].set_xlabel(r"$Re$")
ax[ii].set_ylabel(r"$H_1$")

ax[ii].plot(F0["Re"],F0["H1"], style = LS.Blue[0], label = r"$El = 0.00$")
ax[ii].plot(F1["Re"],F1["H1"], style = LS.Blue[1], label = r"$El = 0.25$")

ax[ii].set_limit( xrange = (0.0, 20.0, 4.0, 0.50), yrange = (0.0, 6.0, 1.0, 0.25))
ax[ii].legend()
# ax[ii].subscript()




# ii = 1
# ax[ii].set_xlabel(r"$Re$")
# ax[ii].set_ylabel(r"$H_2$")

# ax[ii].plot(F0["Re"],F0["H2"], style = LS.Blue[0], label = r"$El = 0.00$")
# ax[ii].plot(F1["Re"],F1["H2"], style = LS.Blue[1], label = r"$El = 0.25$")

# ax[ii].set_limit( xrange = (0.0, 20.0, 4.0, 0.50), yrange = (0.0, 16.0, 2.0, 0.50))
# ax[ii].legend()
# ax[ii].subscript()





plt.savefig("Test.png", dpi = 300)
plt.show()