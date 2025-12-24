import matplotlib.pyplot as plt
import numpy as np
import cv2

# ------------Transformation parameters---------------------
original = [[10,9], [16,9], [6,17]]
shift1 = [[-5,4.5], [-8, 4.5],  [-3,8.5]]
shift2 = [ [-4.5,-5], [-4.5,-8],  [-8.5,-3]]

# ----------------points-------------------------
outer_dofda3 =[[2,2],[2,3], [4,3], [2,4], [2,5], [3,6], [4,6], [3,8], [3,11],
    [6,15], [6,17], [8,19], [11,19], [12,17], [12,16], [14,16],
    [14,17], [15,19], [18,19], [20,17],[20,15], [23,11], [23,8], 
    [22,6], [23,6], [24,5], [24,4], [22,3], [24,3], [24,2], [2,2]]

batn_dofda3 = [[4,6], [9,2], [8,5], [8,8], [10,9],[16,9], [18,8],[18,5], [17,2], [22,6]]

bo2_dofda3 = [[6,13], [7,12], [19,12], [20,13]]


dofda3_eye_left = [[8,14], [7,15], [7,17], [8,18], [10,18], [11,17], [11,15] , [10,14], [8,14]  ]
dofda3_eye_right = [[16,14], [15,15], [15,17], [16,18], [18,18], [19,17], [19,15] , [18,14], [16,14] ]

dofda3_eye_pupil_left = [[8,16], [8,17], [9,17], [9,16], [8,16] ]
dofda3_eye_pupil_right = [[16,16], [16,17], [17,17], [17,16], [16,16] ]


dofda3 = [outer_dofda3, bo2_dofda3, batn_dofda3, dofda3_eye_left, dofda3_eye_right, dofda3_eye_pupil_left, dofda3_eye_pupil_right]

# =========================transformation==========================
src_points =np.float32(original)
dest_points1 = np.float32(shift1)
dest_points2 = np.float32(shift2)

transformation_matrix1 = cv2.getAffineTransform(src_points,dest_points1)
transformation_matrix1 = np.delete(transformation_matrix1, 2, axis=1)

transformation_matrix2 = cv2.getAffineTransform(src_points,dest_points2)
transformation_matrix2 = np.delete(transformation_matrix2, 2, axis=1)


reflected_dofda3 = [[] for i in range(len(dofda3))]
rotated_dofda3 =[[] for i in range(len(dofda3))]


# -------------------------show outline------------------------------------
def show_outline(outline):

    x_cooordinates = [p[0] for p in outline]
    y_coordinates = [p[1] for p in outline]


    plt.plot(x_cooordinates, y_coordinates , 'black', linewidth=2)


# -----------------------plotting-----------------------------------------
def graph():
    plt.title('Plotting from a 2D List')
    plt.axvline(0,color="black")
    ax = plt.gca()

    #move both axes to the origin
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")

    #hide the other two axes
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks(range(-12,25 ))
    plt.yticks(range(-12,25))
    plt.legend()
    plt.grid(True)

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











