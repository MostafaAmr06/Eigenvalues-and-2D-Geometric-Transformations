import numpy as np
import cv2 


# ------------Transformation parameters---------------------
original = [[10,9], [16,9], [6,17]]
shift1 = [[-5,4.5], [-8, 4.5],  [-3,8.5]]
shift2 = [ [-4.5,-5], [-4.5,-8],  [-8.5,-3]]

# =========================transformation==========================
src_points =np.float32(original)
dest_points1 = np.float32(shift1)
dest_points2 = np.float32(shift2)

transformation_matrix1 = cv2.getAffineTransform(src_points,dest_points1)
transformation_matrix1 = np.delete(transformation_matrix1, 2, axis=1)

transformation_matrix2 = cv2.getAffineTransform(src_points,dest_points2)
transformation_matrix2 = np.delete(transformation_matrix2, 2, axis=1)