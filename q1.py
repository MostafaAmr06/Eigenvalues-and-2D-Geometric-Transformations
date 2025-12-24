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
    for point in shape:
        result_point = np.matmul(transformation_matrix1, point)
        reflected_dofda3[i].append(list(result_point))

        result_point = np.matmul(transformation_matrix2, point)
        rotated_dofda3[i].append(list(result_point))

    # 1. Fill Outer Body (Green)
    plt.fill([p[0] for p in dofda3[0]], [p[1] for p in dofda3[0]], color='#4CAF50')
    plt.fill([p[0] for p in reflected_dofda3[0]], [p[1] for p in reflected_dofda3[0]], color='#4CAF50')
    plt.fill([p[0] for p in rotated_dofda3[0]], [p[1] for p in rotated_dofda3[0]], color='#4CAF50')

    # 2. Fill Belly (Light Green)
    plt.fill([p[0] for p in dofda3[2]], [p[1] for p in dofda3[2]], color='#C8E6C9')
    plt.fill([p[0] for p in reflected_dofda3[2]], [p[1] for p in reflected_dofda3[2]], color='#C8E6C9')
    plt.fill([p[0] for p in rotated_dofda3[2]], [p[1] for p in rotated_dofda3[2]], color='#C8E6C9')

    # 3. Fill Eyes (White)
    for eye_idx in [3, 4]:
        plt.fill([p[0] for p in dofda3[eye_idx]], [p[1] for p in dofda3[eye_idx]], color='#FFFFFF')
        plt.fill([p[0] for p in reflected_dofda3[eye_idx]], [p[1] for p in reflected_dofda3[eye_idx]], color='#FFFFFF')
        plt.fill([p[0] for p in rotated_dofda3[eye_idx]], [p[1] for p in rotated_dofda3[eye_idx]], color='#FFFFFF')

    # 4. Fill Pupils (Left: Black, Right: Gray)
    # Left Pupil (Index 5)
    plt.fill([p[0] for p in dofda3[5]], [p[1] for p in dofda3[5]], color='#000000')
    plt.fill([p[0] for p in reflected_dofda3[5]], [p[1] for p in reflected_dofda3[5]], color='#000000')
    plt.fill([p[0] for p in rotated_dofda3[5]], [p[1] for p in rotated_dofda3[5]], color='#000000')
    
    # Right Pupil (Index 6) - Changed to Gray
    plt.fill([p[0] for p in dofda3[6]], [p[1] for p in dofda3[6]], color='#414141')
    plt.fill([p[0] for p in reflected_dofda3[6]], [p[1] for p in reflected_dofda3[6]], color="#414141")
    plt.fill([p[0] for p in rotated_dofda3[6]], [p[1] for p in rotated_dofda3[6]], color='#414141')

    # Finally, draw the black outlines
    show_outline(dofda3[i])
    show_outline(reflected_dofda3[i])
    show_outline(rotated_dofda3[i])
    stats_text = f"Transformation Matrix 2:\n{np.round(transformation_matrix1.astype(float), 2)}\n\nTransformation Matrix 2:\n{np.round(transformation_matrix2.astype(float), 2)}"
    plt.gcf().text(0.6, 0.2, stats_text, fontsize=9,  verticalalignment='center')


graph()
plt.show()










