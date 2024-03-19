import time
def getMidPoint(p1,p2):
    x = float((p1[0]+p2[0])/2 )
    y = float((p1[1]+p2[1])/2)
    pout = (x,y)
    return pout

def BezierN(points, iterasi, iterasiMax):
    if (iterasi >= iterasiMax):
        return []
    else:
        q = points
        left = [q[0]]
        right = [q[-1]]
        while len(q) > 1:
            temp = q
            q = [getMidPoint(temp[i], temp[i+1]) for i in range(len(temp)-1)]
            left.append(q[0])
            right.append(q[-1])
        right.reverse()
        if iterasi == 0:
            iterasi += 1
            return [points[0]] + BezierN(left, iterasi, iterasiMax) + [right[0]] + BezierN(right, iterasi, iterasiMax) + [points[-1]]
        else:
            iterasi += 1
            return BezierN(left, iterasi, iterasiMax) + [right[0]] + BezierN(right, iterasi, iterasiMax)

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

titik = int(input("n = "))
x = []
y = []
for i in range(titik):
    x.append(int(input("x" + str(i + 1) + " = ")))
    y.append(int(input("y" + str(i + 1) + " = ")))

iterasi = int(input("Iterasi: "))

tstart = time.time()
BezierBruteForce((x[0],y[0]), (x[1],y[1]), (x[2],y[2]), iterasi)
tstop = time.time()
print("Brute Force:", (tstop - tstart) * 1000)
# print(b)

tstart = time.time()
BezierN([(x[0],y[0]), (x[1],y[1]), (x[2],y[2])],0, iterasi)
tstop = time.time()
print("DNC:", (tstop - tstart) * 1000)
# print(a)
