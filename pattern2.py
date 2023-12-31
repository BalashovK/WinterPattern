import numpy as np
import matplotlib.pyplot as plt
a = np.arange(19, dtype="int").reshape(19, 1)
y, x = np.where(np.bitwise_or(((a + a.T) % 6 == 3), ((a - a.T) % 6 == 3)))
plt.scatter(x, y, marker='*')
plt.axis('off')
plt.show()