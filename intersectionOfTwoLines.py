import matplotlib.pyplot as plt

from utils.drawFigure import draw_line
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
    data_test = ["test/intersectionOfTwoLines/1.txt",
                 "test/intersectionOfTwoLines/2.txt",
                 "test/intersectionOfTwoLines/3.txt",
                 "test/intersectionOfTwoLines/4.txt",
                 "test/intersectionOfTwoLines/5.txt",
                 "test/intersectionOfTwoLines/6.txt"]
    for data in data_test:
        dots = get_dots(data)
        dot11 = dots[0]
        dot12 = dots[1]
        dot21 = dots[2]
        dot22 = dots[3]
        draw_line(dot11, dot12, "")
        draw_line(dot21, dot22, "")
        A1, B1, C1 = canonical_equation(dot11, dot12)
        A2, B2, C2 = canonical_equation(dot21, dot22)
        result_dot11 = hyperplane_and_dot(dot11, A2, B2, C2)
        result_dot12 = hyperplane_and_dot(dot12, A2, B2, C2)
        result_dot21 = hyperplane_and_dot(dot21, A1, B1, C1)
        result_dot22 = hyperplane_and_dot(dot22, A1, B1, C1)
        result = ""
        if result_dot11 * result_dot12 <= 0 and result_dot21 * result_dot22 <= 0:
            result = "YES"
        else:
            result = "NO"
        plt.title(result)
        plt.show()

if __name__ == "__main__":
    main()

