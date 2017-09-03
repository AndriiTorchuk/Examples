"""
Exercise 6. Two columns.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.figure('Two columns')
x = np.linspace(1, 10, 50)
y_cos = np.cos(x)
y_sin = np.sin(x)
plt.subplot(1, 2, 1)
plt.plot(x, y_cos, 'r--')
plt.title('cos')
plt.subplot(1, 2, 2)
plt.plot(x, y_cos, 'b-')
plt.title('sin')
plt.show()