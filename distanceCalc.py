import math

# calculates the Distance for the simulation.
def calcDist(x1, x2, y1, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return dist


# function to calculate the X and Y of E given the distances. Calculates therefor using a reversed distance formula. Read more here: https://en.wikipedia.org/wiki/Distance

def calculateXandYofE(B, C, ae, be, ce):
    if B[0] == 0:
        x = ((ae**2 + (C[0]**2)) - (ce**2))/(C[0]*2)
        y = math.sqrt((ae**2) - (x**2))
        computed_dist = math.sqrt((x - C[0])**2 + (y - C[1])**2)
    else:
        x = ((ae**2 + (B[0]**2)) - (be**2))/(B[0]*2)
        y = math.sqrt((ae**2) - (x**2))
        computed_dist = math.sqrt((x - C[0])**2 + (y - C[1])**2)
    if abs(computed_dist - ce) < 0.1:
        return round(x), round(y)
    else:
        return round(x), round((-y))


def distCalc(B, C, ae, be, ce):
    E = calculateXandYofE(B, C, ae, be, ce)
    
    return E

def cordCalc(A, B, C, E):

    ae = calcDist(A[0], E[0], A[1], E[1])
    be = calcDist(B[0], E[0], B[1], E[1])
    ce = calcDist(C[0], E[0], C[1], E[1])

    E = calculateXandYofE(B, C, ae, be, ce)

    return E, ae, be, ce

if __name__ == "__main__":
    print(cordCalc((0, 0), (0, 3), (5, 0), (3, 2)))