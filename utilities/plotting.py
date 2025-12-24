import matplotlib.pyplot as plt
import numpy as np


# -------------------------show outline------------------------------------
def show_outline(outline):

    x_cooordinates = [p[0] for p in outline]
    y_coordinates = [p[1] for p in outline]

    plt.plot(x_cooordinates, y_coordinates , 'black', linewidth=2)


# ------------------------------- graph -------------------------------
def graph():

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
    plt.grid(True, alpha=0.2)


