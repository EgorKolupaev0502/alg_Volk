from matplotlib import pyplot as plt


def draw_line(dot1, dot2, label):
    # print(dot1, dot2)
    if label == "":
        plt.plot([dot1[0], dot2[0]], [dot1[1], dot2[1]])
    else:
        plt.plot([dot1[0], dot2[0]], [dot1[1], dot2[1]], label=label)

def draw_triangle(dot1, dot2, dot3):
    print(dot1, dot2, dot3)
    draw_line(dot1, dot2, "")
    draw_line(dot3, dot1, "")
    draw_line(dot2, dot3, "")