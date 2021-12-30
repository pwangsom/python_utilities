from numpy import linalg as lng
import numpy as np

ref = np.array((0,0,0))

c0 = np.array((0.28,0.36,0.30))
dist = lng.norm(ref - c0)
print(dist)

c1 = np.array((0.04,0.07,0.65))
dist = lng.norm(ref - c1)
print(dist)

c2 = np.array((0.73,0.80,0.59))
dist = lng.norm(ref - c2)
print(dist)

c3 = np.array((0.32,0.81,0.60))
dist = lng.norm(ref - c3)
print(dist)

c4 = np.array((0.63,0.71,0.34))
dist = lng.norm(ref - c4)
print(dist)

c5 = np.array((0.07,0.10,0.31))
dist = lng.norm(ref - c5)
print(dist)

c6 = np.array((0.41,0.49,0.57))
dist = lng.norm(ref - c6)
print(dist)

c7 = np.array((0.17,0.27,0.59))
dist = lng.norm(ref - c7)
print(dist)