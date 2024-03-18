# Impementation

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
        iterate += 1
        return [p0] + BezierKuadratik(p0, q0, r0, iterate, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate, iterateMax) + [p2]
    elif iterate < iterateMax:
        iterate += 1
        return BezierKuadratik(p0, q0, r0, iterate, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate, iterateMax)
    else:
        return []
    
print(BezierKuadratik((0,0),(1,1),(2,0),0,1))
print(BezierKuadratik((0,0),(1,1),(2,0),0,2))