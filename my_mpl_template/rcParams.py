import matplotlib.pyplot      as     plt


def set_labelsize(val = 18): plt.rcParams.update({"axes.labelsize": val})




def graph_mode(mode = "publication"):

	if mode.lower() == "publication":

		plt.rcParams.update({'text.usetex'         : True  } )
		plt.rcParams.update({'text.latex.preamble' :r'\usepackage{nicefrac}'})

		plt.rcParams.update({'axes.linewidth'      :  3.0  } )
		plt.rcParams.update({'axes.labelsize'      : 18.0  } )
		plt.rcParams.update({'font.size'           : 16.0  } )
		plt.rcParams.update({'font.weight'         :'bold' } )

		plt.rcParams.update({'xtick.top'           : True })
		plt.rcParams.update({'xtick.bottom'        : True })
		plt.rcParams.update({'xtick.major.size'    : 8.0  })
		plt.rcParams.update({'xtick.minor.size'    : 4.0  })
		plt.rcParams.update({'xtick.major.width'   : 2.5  })
		plt.rcParams.update({'xtick.minor.width'   : 2.5  })
		plt.rcParams.update({'xtick.direction'     : 'in' })
		plt.rcParams.update({'xtick.minor.visible' : True })
		plt.rcParams.update({'xtick.major.pad'     : 3    })

		plt.rcParams.update({'ytick.left'          : True })
		plt.rcParams.update({'ytick.right'         : True })
		plt.rcParams.update({'ytick.major.size'    : 8.0  })
		plt.rcParams.update({'ytick.minor.size'    : 4.0  })
		plt.rcParams.update({'ytick.major.width'   : 2.5  })
		plt.rcParams.update({'ytick.minor.width'   : 2.5  })
		plt.rcParams.update({'ytick.direction'     : 'in' })
		plt.rcParams.update({'ytick.minor.visible' : True })

		plt.rcParams.update({'legend.frameon'      : False})
		plt.rcParams.update({'legend.fontsize'     : 16   })

	elif mode.lower() == "presentation" :

		plt.rcParams.update({'text.usetex'         : True  } )
		plt.rcParams.update({'text.latex.preamble' :r'\usepackage{nicefrac}'})

		plt.rcParams.update({'axes.linewidth'      :  4.0  } )
		plt.rcParams.update({'axes.labelsize'      : 20.0  } )
		plt.rcParams.update({'font.size'           : 18.0  } )
		plt.rcParams.update({'font.weight'         :'bold' } )

		plt.rcParams.update({'xtick.top'           : True })
		plt.rcParams.update({'xtick.bottom'        : True })
		plt.rcParams.update({'xtick.major.size'    :10.0  })
		plt.rcParams.update({'xtick.minor.size'    : 6.0  })
		plt.rcParams.update({'xtick.major.width'   : 3.5  })
		plt.rcParams.update({'xtick.minor.width'   : 3.5  })

		plt.rcParams.update({'xtick.direction'     : 'in' })
		plt.rcParams.update({'xtick.minor.visible' : True })
		plt.rcParams.update({'xtick.major.pad'     : 3    })

		plt.rcParams.update({'ytick.left'          : True })
		plt.rcParams.update({'ytick.right'         : True })
		plt.rcParams.update({'ytick.major.size'    :10.0  })
		plt.rcParams.update({'ytick.minor.size'    : 6.0  })
		plt.rcParams.update({'ytick.major.width'   : 3.5  })
		plt.rcParams.update({'ytick.minor.width'   : 3.5  })
		plt.rcParams.update({'ytick.direction'     : 'in' })
		plt.rcParams.update({'ytick.minor.visible' : True })

		plt.rcParams.update({'legend.frameon'      : False})
		plt.rcParams.update({'legend.fontsize'     : 16   })



# Define default graph mode.

graph_mode()
