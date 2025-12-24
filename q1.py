import matplotlib.pyplot as plt
import numpy as np
from utilities.frog_data import dofda3
from utilities.find_transformation import transformation_matrix1, transformation_matrix2
from utilities.plotting import graph,show_outline


reflected_dofda3 = [[] for i in range(len(dofda3))]
rotated_dofda3 =[[] for i in range(len(dofda3))]


# -----------------------plotting-----------------------------------------

for i in range(len(dofda3)):
    shape = np.array(dofda3[i])
    for point in shape :

        result_point = np.matmul(transformation_matrix1,point)
        reflected_dofda3[i].append(list(result_point))

        result_point = np.matmul(transformation_matrix2,point)
        rotated_dofda3[i].append(list(result_point))
    show_outline(dofda3[i])
    show_outline(reflected_dofda3[i])
    show_outline(rotated_dofda3[i])

graph()
plt.show()











