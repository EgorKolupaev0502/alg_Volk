def canonical_equation(dot1, dot2):
    A = dot1[1] - dot2[1]
    B = dot2[0] - dot1[0]
    C = dot1[0] * dot2[1] - dot2[0] * dot1[1]
    return A, B, C