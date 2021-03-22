import numpy as np

ref = np.array((0, 0, 0))

"""
0.06,0.09,0.46
0.73,0.81,0.57
0.18,0.27,0.61
0.21,0.28,0.28
0.46,0.52,0.6
0.03,0.06,0.68
0.32,0.43,0.43
0.6,0.7,0.32
0.33,0.81,0.6
0.06,0.09,0.2
"""

c0 = np.array((0.06,0.09,0.46))
dist = np.linalg.norm(ref-c0)
print(dist)

c1 = np.array((0.73,0.81,0.57))
dist = np.linalg.norm(ref-c1)
print(dist)

c2 = np.array((0.18,0.27,0.61))
dist = np.linalg.norm(ref-c2)
print(dist)

c3 = np.array((0.21,0.28,0.28))
dist = np.linalg.norm(ref-c3)
print(dist)

c4 = np.array((0.46,0.52,0.6))
dist = np.linalg.norm(ref-c4)
print(dist)

c5 = np.array((0.03,0.06,0.68))
dist = np.linalg.norm(ref-c5)
print(dist)

c6 = np.array((0.32,0.43,0.43))
dist = np.linalg.norm(ref-c6)
print(dist)

c7 = np.array((0.6,0.7,0.32))
dist = np.linalg.norm(ref-c7)
print(dist)

c8 = np.array((0.33,0.81,0.6))
dist = np.linalg.norm(ref-c8)
print(dist)

c9 = np.array((0.06,0.09,0.2))
dist = np.linalg.norm(ref-c9)
print(dist)
