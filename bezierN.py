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
        print(q)
        left = [q[0]]
        right = [q[-1]]
        while len(q) > 1:
            temp = q
            q = [getMidPoint(temp[i], temp[i+1]) for i in range(len(temp)-1)]
            left.append(q[0])
            right.append(q[-1])
            print(q)
        if iterasi == 0:
            iterasi += 1
            return [points[0]] + BezierN(left, iterasi, iterasiMax) + [left[-1]] + BezierN(right, iterasi, iterasiMax) + [points[-1]]
        else:
            iterasi += 1
            return BezierN(left, iterasi, iterasiMax) + [left[-1]] + BezierN(right, iterasi, iterasiMax)

print(BezierN([(0,0), (0.5, 0.5), (1,1), (1.5 , 0.5), (2,0)], 0, 3))