import math
import numpy as np


step = 1/10000

def function_demi_cercle(x):
    return math.sqrt(4-x*x)

resultat = 0

for i in np.arange(0, 2+step, step):
    resultat += function_demi_cercle(i) * step

print(resultat) # 3.1416922378180026
print(np.pi)    # 3.141592653589793