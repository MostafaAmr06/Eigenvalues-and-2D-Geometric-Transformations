import cv2
import numpy as np
import matplotlib.pyplot as plt


beit_orignal = np.float32([[1,1], [0,3], [3,5]])
beit_transformed = np.float32([[5.25, -2], [5,-6], [5.75, -10]])
beit_full = np.float32([[1,1], [1,3],[0,3], [3,5], [4,4.25], [4,4.5], [4.5,4.5], [4.5,4], [6,3], [5,3], [5,1], [1,1]])

M = cv2.getAffineTransform(beit_orignal, beit_transformed)

B = M[:, :2]
V = M[:, 2].reshape(2, 1)
B[np.abs(B) < 0.001] = 0
V[np.abs(V) < 0.001] = 0

print(B)
print(V)

transformed = np.dot(B, beit_full.T) + V
plt.plot(beit_full[:, 0], beit_full[:, 1], color='blue', label='Original')
plt.plot(transformed[0, :], transformed[1, :], color='red', label='Transformed')
plt.axhline(0, color='black')

stats_text = f"B matrix:\n{np.round(B.astype(int), 2)}\n\nV vector:\n{np.round(V.astype(int), 2)}"
plt.gcf().text(0.2, 0.3, stats_text, fontsize=10, bbox=dict(facecolor='black', alpha=0.4), verticalalignment='center')

plt.grid()
plt.show()