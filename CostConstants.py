# Costs for each component in the process.

from Conversions import kg_to_lb

# Costs in $/pound
LB_COST_WATER = .00018
LB_COST_CSL = .065
LB_COST_GLUCOSE = .15
LB_COST_CaCO4 = .15
LB_COST_TWEEN80 = 1.30
LB_COST_BACTERIA = 1.00

LB_COST_LA = .90

# Costs in $/kg
KG_COST_WATER = kg_to_lb(LB_COST_WATER)
KG_COST_CSL = kg_to_lb(LB_COST_CSL)
KG_COST_GLUCOSE = kg_to_lb(LB_COST_GLUCOSE)
KG_COST_CaCO4 = kg_to_lb(LB_COST_CaCO4)
KG_COST_TWEEN80 = kg_to_lb(LB_COST_TWEEN80)
KG_COST_BACTERIA = kg_to_lb(LB_COST_BACTERIA)

KG_COST_LA = kg_to_lb(LB_COST_LA)
