from ChemConstants import C_BACT_INIT, C_GLUC_INIT, C_LA_INIT, dBACT_dT_INIT, TIME_INIT, FERMENT_CONST, CHEMICALS
from CostConstants import KG_COST_BACTERIA, KG_COST_GLUCOSE, KG_COST_LA, KG_COST_WATER
from Conversions import g_to_kg

import logging

logging.basicConfig(level=logging.DEBUG, filename="GrowthCurve_Log", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

FERMENT_WATER_VOL = FERMENT_CONST['Water Volume']
FERMENT_RUNTIME = FERMENT_CONST['Runtime']

C_BACT_VAR = C_BACT_INIT
C_GLUC_VAR = C_GLUC_INIT
C_LA_VAR = C_LA_INIT
dBACT_dT_VAR = dBACT_dT_INIT
TIME_VAR = TIME_INIT
C_LA_CACHE = []
C_GLUC_CACHE = []
C_BACT_CACHE = []

while C_GLUC_VAR >= 10.0:
    TIME_VAR += 1
    dBACT_dT_VAR = ((C_GLUC_VAR*.54)/(C_GLUC_VAR+100))*C_BACT_VAR*(1-(C_LA_VAR/100))
    C_BACT_VAR += dBACT_dT_VAR
    C_LA_VAR = .9*(C_GLUC_INIT - C_GLUC_VAR) + C_LA_INIT
    C_GLUC_VAR = -(((C_BACT_VAR-C_BACT_INIT)/.4)-C_GLUC_INIT)
    C_LA_CACHE.append(C_LA_VAR)
    C_GLUC_CACHE.append(C_GLUC_VAR)
    C_BACT_CACHE.append(C_BACT_VAR)

# masses purchased in grams
G_MASS_BACT = C_BACT_INIT * FERMENT_WATER_VOL
G_MASS_GLUC = (C_GLUC_INIT - C_GLUC_VAR) * FERMENT_WATER_VOL
G_MASS_LA = (C_LA_VAR - C_LA_INIT) * FERMENT_WATER_VOL

KG_MASS_BACT = g_to_kg(G_MASS_BACT)
KG_MASS_GLUC = g_to_kg(G_MASS_GLUC)
KG_MASS_LA = g_to_kg(G_MASS_LA)
KG_MASS_WATER = FERMENT_WATER_VOL * CHEMICALS["Water"][1]

BATCH_COST_BACT = KG_MASS_BACT * KG_COST_BACTERIA
BATCH_COST_GLUC = KG_MASS_GLUC * KG_COST_GLUCOSE
BATCH_COST_LA = KG_MASS_LA * KG_COST_LA
BATCH_COST_WATER = KG_MASS_WATER * KG_COST_WATER

C_GLUC_FINAL = C_GLUC_CACHE[FERMENT_RUNTIME]
C_BACT_FINAL = C_BACT_CACHE[FERMENT_RUNTIME]
C_LA_FINAL = C_LA_CACHE[FERMENT_RUNTIME]

# logging.info(str(TIME_VAR), str(dBACT_dT_VAR), str(C_BACT_VAR), str(C_LA_VAR), str(C_GLUC_VAR))
logging.info("TIME_VAR = %s, dBACT_dT_VAR = %s, C_BACT_VAR = %s, C_LA_VAR = %s, C_GLUC_VAR = %s",
             TIME_VAR, dBACT_dT_VAR, C_BACT_VAR, C_LA_VAR, C_GLUC_VAR)

logging.info("COSTS PER BATCH: Bacteria = %s, Glucose = %s, Water = %s, Lactic Acid = %s",
             BATCH_COST_BACT, BATCH_COST_GLUC, BATCH_COST_WATER, BATCH_COST_LA)

print C_LA_CACHE