import numpy as np
import matplotlib.pyplot as plt
a = np.zeros(460, "bool")
a[::6] = True
b = a.reshape(20, 23)
c = b[0:19,3:22]
d = np.flipud(c)
f = np.bitwise_or(c,d)
y, x = np.where(f)
plt.scatter(x, y, marker='*')
plt.axis('off')
plt.show()