import numpy as np

import matplotlib.pyplot as plt

h = plt.hist(np.random.triangular(30, 130, 1300, 39873), bins=200,
             density=True)
plt.show()