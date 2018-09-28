from FluidStream import *
# List of chemicals and their constant properties

CHEMICALS_KEY_GUIDE = ['MW'    , 'Density']
CHEMICALS = {
'Bacteria'			: ['NA'    , 1.05  ],
'Calcium Carbonate' : [100.087 , 2.71  ],
'Calcium Lactate'   : [218.22  , 1.494 ],
'Corn Steep Liquor' : ['NA'	   , 1.2326],
'Glucose'			: [180.156 , 1.54  ],
'Lactic Acid'		: [90.08   , 1.206 ],
'Octanol'           : [130.231 , .824  ],
'Tween 80'			: ['NA'	   , 1.07  ],
'Water'				: [18.015  , .995  ],
'Water/Glucose 10%'	: [34.2291 , 1.0375]
}

SOLVE_FOR_PRODUCTION = True
PRODUCTION_TO_SOLVE = 100000000


def convert_mass_to_concentration(fluidStream, component):
    total_mass = fluidStream.TotalMass


def component_mass_to_volume(mass, component):
    component_density = CHEMICALS[component][1]
    component_volume = mass*component_density
    return component_volume


# Bacterial Growth Curve

# TIME_INIT --> hours
TIME_INIT = 0

# C_BACT_INIT --> g/L
C_BACT_INIT = .7

# C_GLUC_INIT --> g/L
C_GLUC_INIT = 100.0

# C_LA_INIT --> g/L
C_LA_INIT = 12.57

# C_TWEEN_INIT --> g/L
C_TWEEN_INIT = 1.0

# dBACT_dT -- > g/L*h
dBACT_dT_INIT = 0.0

FERMENT_IN = {
'Bacteria Concentration' : C_BACT_INIT,
'Glucose Concentration'  : C_GLUC_INIT,
'Lactic Acid Concentration' : C_LA_INIT,
'Tween 80 Concentration' : C_TWEEN_INIT
}

# HOLDING TANK SPECS
# Initial Fermentation Water Charge in Liters
FERMENT_WATER_VOL = 750000
# Number of Fermentation Vessels
FERMENT_VESSEL_COUNT = 4
# Runtime of Fermentation Process
FERMENT_RUNTIME = 32
# Downtime of Fermentation Process
FERMENT_DOWNTIME = 8
# Total Runtime of Each Fermentation Batch
FERMENT_BATCH_TIME = FERMENT_RUNTIME + FERMENT_DOWNTIME

FERMENT_CONST = {
'Water Volume' : FERMENT_WATER_VOL,
'Vessel Count' : FERMENT_VESSEL_COUNT,
'Runtime'      : FERMENT_RUNTIME,
'Downtime'     : FERMENT_DOWNTIME,
'Batch Time'   : FERMENT_BATCH_TIME }

# Acid Dissociation Constant Ka
SALTS_pKa = 3.86
SALTS_Ka = pow(10, (-1*SALTS_pKa))
MAX_pH = 3.8
pKa_pH_CALC = pow(10, (SALTS_pKa - MAX_pH))
MW_SALT = CHEMICALS['Calcium Lactate'][0]
MW_LA = CHEMICALS['Lactic Acid'][0]



