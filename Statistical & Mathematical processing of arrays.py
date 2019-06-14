import numpy as np
import matplotlib.pyplot as plt

axes_values = np.arange(-100,100,10) #x coordinates on graph

dx, dy = np.meshgrid(axes_values,axes_values)

# Meshgrid groups the values with itsef again and again
# like cartesian cross product

print("dx")
print(dx)

print("dy")
print(dy)

function = 2*dx+3*dy
#creating another numpy function using np.cos

function2 = np.cos(dx)+np.cos(dy)

#plot function on graph
print("function is")
print(function)

plt.imshow(function)
#imshow is a function of plt used to plot a graph on colossal chart
plt.title('function of plot 2*dx+3*dy')
plt.colorbar()
plt.savefig('myfig.png')

plt.imshow(function2)
plt.title('function cos plot')
plt.colorbar()
plt.savefig('myfig2.png')
