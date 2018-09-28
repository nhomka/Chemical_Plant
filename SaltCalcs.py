from ChemConstants import pKa_pH_CALC, FERMENT_WATER_VOL, MW_SALT, MW_LA, FERMENT_RUNTIME
from GrowthCurve import C_LA_CACHE
from Conversions import g_to_kg, kg_to_g

import matplotlib.pyplot as plt

C_LA_VAR = C_LA_CACHE[0]
MOLES_LA_VAR = C_LA_VAR*(FERMENT_WATER_VOL/MW_LA)
MOLES_SALT_VAR = 0
MASS_SALT_VAR = 0
TIME_CACHE = []
MASS_SALT_CACHE = []

for i in range(0, len(C_LA_CACHE)):
    C_LA_VAR = C_LA_CACHE[i]
    MOLES_LA_VAR = C_LA_VAR * (FERMENT_WATER_VOL / MW_LA)
    MOLES_SALT_VAR = (MOLES_LA_VAR / 2) / pKa_pH_CALC
    MASS_SALT_TEMP = g_to_kg(MOLES_SALT_VAR * MW_SALT)
    MASS_PER_HR = MASS_SALT_TEMP - MASS_SALT_VAR
    MASS_SALT_VAR = MASS_SALT_TEMP
    TIME_VAR = i
    TIME_CACHE.append(i)
    MASS_SALT_CACHE.append(MASS_SALT_VAR)

C_SALT_OUT = kg_to_g(MASS_SALT_CACHE[FERMENT_RUNTIME - 1]) / FERMENT_WATER_VOL

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = TIME_CACHE
y = MASS_SALT_CACHE
ax.scatter(x, y)
plt.show()
