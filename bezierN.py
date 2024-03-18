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
            return [points[0]] + BezierN(left, iterasi, iterasiMax) + [left[-1]] + BezierN(right, iterasi, iterasiMax) + [points[-1]]
        else:
            iterasi += 1
            return BezierN(left, iterasi, iterasiMax) + [left[-1]] + BezierN(right, iterasi, iterasiMax)

def bruteForceN(points, iterasi):
    n = pow(2, iterasi)
    delta = 1 / n
    t = 0
    b = []
    for i in range(n):
        p = [(pow(1-t, 3)*points[0][i] + 3*pow(1-t, 2)*t*points[1][i] + 3 * (1-t) * pow(t, 2) * points[2][i] + pow(t, 3) * points[3][i]) for i in range(2)]
        b.append((p[0], p[1]))
        t += delta
    p = [points[3][i] for i in range(2)]
    b.append((p[0], p[1]))
    return b

tstart = time.time()
b = bruteForceN([(1,0), (3, 3), (5,3)], 3)
tstop = time.time()
print("Brute Force:", (tstop - tstart) * 1000)
print(b)

tstart = time.time()
a = BezierN([(1,0), (3, 3), (5,3)],0, 3)
tstop = time.time()
print("DNC:", (tstop - tstart) * 1000)
print(a)
