#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,5),dpi=300) #required to save as .eps

working_directory = "/Users/avellaneda/Desktop/Analyse python/new/"
fname = working_directory + "plot_data_PC_32h_norm.csv"

data = np.loadtxt(fname, delimiter=";", skiprows=1)


x = data[:,1]
i = np.size(data, 1)

for col in np.arange(i):
    if col > 1:
        y = data[:, col]
        #plt.scatter(x, y) # you can comment in if points are needed
        legend = col - 2
        plt.plot(x, y, label = str(legend) + "min")

plt.xlabel("Distance in microns")
plt.ylabel("Photoconverted Dendra intensity (arbitrary units)")
plt.title('Mitochondria movement')
plt.legend()
plt.ylim([0,3])

plt.savefig(working_directory + "_plot.eps", format = "eps") #if you want to save the plot to the save location of data uncomment line

plt.show() # always needs to be at the end, after plt.savefig() otherwise fig is not saved correctly


# In[6]:


from scipy.signal import lfilter

n = 20            # larger n gives smoother curves
b = [1.0 / n] * n  # numerator coefficients
a = 1              # denominator coefficient
y_lf_mito = lfilter(b, a, y_mito)
y_lf_actin = lfilter(b, a, y_actin)

plt.plot(x, y_lf_mito)
plt.plot(x, y_lf_actin)
plt.show()


# In[ ]:




