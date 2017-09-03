"""
Exercise 7. Histogram
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(loc=0.0, scale=1.0, size=100)
z = np.random.normal(loc=3.0, scale=1.0, size=100)
plt.hist(np.column_stack((z, x)), bins=10, histtype='bar', color=['b', 'c'], stacked=False)

plt.grid()
plt.show()
