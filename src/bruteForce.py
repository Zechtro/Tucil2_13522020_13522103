import time

def BezierBruteForce(p0, p1, p2, iterasi):
    n = pow(2, iterasi)
    delta = 1 / n
    t = 0
    b = []
    for i in range(n):
        p = [(pow(1-t, 2)*p0[i] + 2*(1-t)*t*p1[i] + pow(t, 2) * p2[i]) for i in range(2)]
        b.append((p[0], p[1]))
        t += delta
    p = [pow(t, 2) * p2[i] for i in range(2)]
    b.append((p[0], p[1]))
    return b

x = []
y = []
for i in range(3):
    x.append(float(input("x" + str(i + 1) + " = ")))
    y.append(float(input("y" + str(i + 1) + " = ")))

iterasi = int(input("Iterasi: "))

tstart = time.time()
a = BezierBruteForce((x[0],y[0]), (x[1],y[1]), (x[2],y[2]), iterasi)
tstop = time.time()
print("Brute Force:", (tstop - tstart) * 1000)

print(a)