import time

def getMidPoint(p1,p2):
    x = float((p1[0]+p2[0])/2 )
    y = float((p1[1]+p2[1])/2)
    pout = (x,y)
    return pout

def BezierKuadratik(p0, p1, p2, iterate, iterateMax):
    q0 = getMidPoint(p0,p1)
    q1 = getMidPoint(p1, p2)
    r0 = getMidPoint(q0,q1)
    if iterate == 0:
        return [p0] + BezierKuadratik(p0, q0, r0, iterate+1, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate+1, iterateMax) + [p2]
    elif iterate < iterateMax:
        return BezierKuadratik(p0, q0, r0, iterate+1, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate+1, iterateMax)
    else:
        return []

x = []
y = []
for i in range(3):
    x.append(int(input("x" + str(i + 1) + " = ")))
    y.append(int(input("y" + str(i + 1) + " = ")))

iterasi = int(input("Iterasi: "))

tstart = time.time()
a = BezierKuadratik((x[0],y[0]), (x[1],y[1]), (x[2],y[2]), 0, iterasi)
tstop = time.time()
print("DNC:", (tstop - tstart) * 1000)
print(a)