import matplotlib.pyplot as plt

from utils.drawFigure import draw_line, draw_triangle
from utils.equations import canonical_equation


def hyperplane_and_dot(dot, A, B, C):
    return A * dot[0] + B * dot[1] + C

def get_dots(name_file):
    dot = []
    with open(name_file, "r") as file:
        for line in file:
            tmp_dot = list(map(int, line.split()))
            dot.append(tmp_dot)
    return dot

def main():
    data_test = ["test/dotAndTriangle/1.txt",
                 "test/dotAndTriangle/2.txt",
                 "test/dotAndTriangle/3.txt"]
    for data in data_test:
        dots = get_dots(data)
        dot = dots[0]
        triangle = [dots[1], dots[2], dots[3]]
        draw_triangle(triangle[0], triangle[1], triangle[2])
        plt.scatter(dot[0], dot[1], color='red', s=100,)
        A1, B1, C1 = canonical_equation(triangle[0], triangle[1])
        A2, B2, C2 = canonical_equation(triangle[1], triangle[2])
        A3, B3, C3 = canonical_equation(triangle[2], triangle[0])
        result = ""
        if hyperplane_and_dot(dot, A1, B1, C1) * hyperplane_and_dot(triangle[2], A1, B1, C1) < 0:
            result = "NO"
        elif hyperplane_and_dot(dot, A2, B2, C2) * hyperplane_and_dot(triangle[0], A2, B2, C2) < 0:
            result = "NO"
        elif hyperplane_and_dot(dot, A3, B3, C3) * hyperplane_and_dot(triangle[1], A3, B3, C3) < 0:
            result = "NO"
        else:
            result = "YES"
        plt.title(result)
        plt.show()

if __name__ == "__main__":
    main()

