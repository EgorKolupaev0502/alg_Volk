# Найдите уравнение прямой, пересекающей два заданных треугольника и делящей каждый из них на равновеликие части.
import numpy as np
import matplotlib.pyplot as plt

from utils.drawFigure import draw_triangle, draw_line


def get_triangles(name_file):
    dot = []
    with open(name_file, "r") as file:
        for line in file:
            tmp_dot = list(map(int, line.split()))
            dot.append(tmp_dot)
    return dot

def get_centroid(dot1, dot2, dot3):
    return [(dot1[0] + dot2[0] + dot3[0]) / 3, (dot1[1] + dot2[1] + dot3[1]) / 3]

def get_line(dot1, dot2):
    x = (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
    c = dot1[1] - x * dot1[0]
    if c < 0:
        x *= -1
        c *= -1
    return [x, c]

def increase_line(dot1, dot2, line):
    if dot1[1] == dot2[1]:
        if dot1[0] > dot2[0]:
            dot1[0] += dot1[0] - dot2[0]
            dot2[0] -= dot1[0] - dot2[0]
        elif dot1[0] < dot2[0]:
            dot1[0] -= dot2[0] - dot1[0]
            dot2[0] += dot2[0] - dot1[0]
        else:
            dot1[0] += 10
            dot2[0] -= 10
    else:
        if dot1[0] > dot2[0]:
            dot1[0] += dot1[0] - dot2[0]
            dot2[0] -= dot1[0] - dot2[0]
            dot1[1] = dot1[0] * line[0] + line[1]
            dot2[1] = dot2[0] * line[0] + line[1]
        elif dot1[0] < dot2[0]:
            dot1[0] -= dot2[0] - dot1[0]
            dot2[0] += dot2[0] - dot1[0]
            dot1[1] = dot1[0] * line[0] + line[1]
            dot2[1] = dot2[0] * line[0] + line[1]
            print(dot1, dot2)
        else:
            if dot1[1] > dot2[1]:
                dot1[1] += dot1[1] - dot2[1]
                dot2[1] -= dot1[1] - dot2[1]
            else:
                dot1[1] -= dot2[1] - dot1[1]
                dot2[1] += dot2[1] - dot1[1]
    return [dot1, dot2]

def main():
    data_test = ["test/twoTrianglesAndLine/1.txt",
                 "test/twoTrianglesAndLine/2.txt",
                 "test/twoTrianglesAndLine/3.txt",
                 "test/twoTrianglesAndLine/4.txt",
                 "test/twoTrianglesAndLine/5.txt"]
    for data in data_test:
        dots_triangle = get_triangles(data)
        centroid1 = get_centroid(dots_triangle[0], dots_triangle[1], dots_triangle[2])
        centroid2 = get_centroid(dots_triangle[3], dots_triangle[4], dots_triangle[5])
        label_line = ""
        equation_line = []
        if centroid1[0] == centroid2[0]:
            label_line = f"x = {centroid1[0]}"
        else:
            equation_line = get_line(centroid1, centroid2)
            label_line = f"{equation_line[0]} * x + {equation_line[1]}"
        print(label_line)
        draw_triangle(dots_triangle[0], dots_triangle[1], dots_triangle[2])
        draw_triangle(dots_triangle[3], dots_triangle[4], dots_triangle[5])
        print(centroid1, centroid2)
        increase_dots = increase_line(centroid1, centroid2, equation_line)
        print(increase_dots)
        draw_line(increase_dots[0], increase_dots[1], label_line)
        draw_line(centroid1, centroid2, label_line)
        plt.show()



if __name__ == "__main__":
    main()

