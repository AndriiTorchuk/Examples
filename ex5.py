"""
Exercise 5. Some more functions.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y_cos = np.cos(x)
y_sin = np.sin(x)
plt.plot(x, y_cos)
plt.plot(x, y_sin)
plt.figure('Trig func')
plt.title('Sin and Cos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()