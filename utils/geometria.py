import numpy as np
import math

class Geometria:
    def __init__(self):
        return

    # Ex:
    # g = Geometria();
    # poligono = [(0,0), (0,1), (1,1), (1,0)]
    # pontoDentro = (0.5,0.5)
    # pontoFora = (1.5,1.5)
    #
    # iss = g.isPointInPoly(poligono, pontoDentro);
    # print(iss)
    def isPointInPoly(self, poly, pt):
        c = False
        i = -1
        l = poly.__len__()
        j = l - 1

        i += 1
        while i < l:
            if (poly[i][1] <= pt[1] and pt[1] < poly[j][1]) or (poly[j][1] <= pt[1] and pt[1] < poly[i][1]):
                if (pt[0] < (poly[j][0] - poly[i][0]) * (pt[1] - poly[i][1]) / (poly[j][1] - poly[i][1]) + poly[i][0]):
                    c = not c
            j = i
            i += 1
        return c
