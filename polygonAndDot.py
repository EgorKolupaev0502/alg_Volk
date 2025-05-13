from math import sqrt
import matplotlib.pyplot as plt
from utils.drawFigure import draw_line
from utils.equations import canonical_equation

def get_polygon(name_file):
    dot = []
    with open(name_file, "r") as file:
        for line in file:
            tmp_dot = list(map(int, line.split()))
            dot.append(tmp_dot)
    return dot

def distance_from_dot_to_dot(dot1, dot2):
    return sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

def distance_from_dot_to_line(dot, A, B, C):
    return abs(A * dot[0] + B * dot[1] + C) / sqrt(A ** 2 + B ** 2)

def projection_dot(dot, A, B, C, distance):
    norm_a = A / sqrt(A ** 2 + B ** 2)
    norm_b = B / sqrt(A ** 2 + B ** 2)
    dot1 = [dot[0] + norm_a * distance, dot[1] + norm_b * distance]
    dot2 = [dot[0] - norm_a * distance, dot[1] - norm_b * distance]
    print(dot1, dot2)
    if A * dot1[0] + B * dot1[1] + C < A * dot2[0] + B * dot2[1] + C:
        return dot1
    return dot2

def dot_in_segment(dot, dot1, dot2):
    if dot1[0] > dot2[0]:
        if dot1[0] < dot[0] or dot2[0] > dot[0]:
            return False
    else:
        if dot1[0] > dot[0] or dot2[0] < dot[0]:
            return False
    return True

def main():
    data_test = ["test/polygonAndDot/1.txt",
                 "test/polygonAndDot/2.txt",
                 "test/polygonAndDot/3.txt",
                 "test/polygonAndDot/4.txt"
                 ]
    for data in data_test:
        dots = get_polygon(data)
        dot = dots[0]
        dots_polygon = dots[1:]
        distance = distance_from_dot_to_dot(dots_polygon[0], dot)
        result_dot = dots_polygon[0]
        for i in range(1, len(dots_polygon)):
            distance_tmp = distance_from_dot_to_dot(dots_polygon[i], dot)
            if distance_tmp < distance:
                distance = distance_tmp
                result_dot = dots_polygon[i]
        for i in range(len(dots_polygon) - 1):
            A, B, C = canonical_equation(dots_polygon[i], dots_polygon[i + 1])
            distance_tmp = distance_from_dot_to_line(dot, A, B, C)
            print(distance, distance_tmp)
            if distance_tmp < distance:
                dot_tmp = projection_dot(dot, A, B, C, distance_tmp)
                if dot_in_segment(dot_tmp, dots_polygon[i], dots_polygon[i + 1]):
                    print(dots_polygon[i], dots_polygon[i + 1], A, B, C, distance_tmp)
                    distance = distance_tmp
                    result_dot = dot_tmp
        A, B, C = canonical_equation(dots_polygon[0], dots_polygon[len(dots_polygon) - 1])
        distance_tmp = distance_from_dot_to_line(dot, A, B, C)
        if distance_tmp < distance:
            dot_tmp = projection_dot(dot, A, B, C, distance_tmp)
            if dot_in_segment(dot_tmp, dots_polygon[len(dots_polygon) - 1], dots_polygon[0]):
                distance = distance_tmp
                result_dot = dot_tmp
        plt.title(distance)
        for i in range(len(dots_polygon) - 1):
            draw_line(dots_polygon[i], dots_polygon[i + 1], "")
        draw_line(dots_polygon[0], dots_polygon[len(dots_polygon) - 1], "")
        plt.scatter(dot[0], dot[1], color='red', s=100)
        draw_line(dot, result_dot, "")
        plt.axis('equal')
        plt.show()

if __name__ == "__main__":
    main()