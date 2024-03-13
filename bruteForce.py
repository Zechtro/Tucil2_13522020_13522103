def BezierBruteForce(p0, p1, p2, iterasi):
    n = pow(2, iterasi)
    delta = 1 / n
    t = 0
    b = []
    for i in range(n):
        print(t)
        p = [(pow(1-t, 2)*p0[i] + 2*(1-t)*t*p1[i] + pow(t, 2) * p2[i]) for i in range(2)]
        b.append((p[0], p[1]))
        t += delta
    p = [pow(t, 2) * p2[i] for i in range(2)]
    b.append((p[0], p[1]))
    return b

print(BezierBruteForce((0,0), (1,1), (2,0), 1))
print(BezierBruteForce((0,0), (1,1), (2,0), 2))
print(BezierBruteForce((0,0), (1,1), (2,0), 3))
