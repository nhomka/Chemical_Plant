import ChemConstants as Chem


class FluidStream:

    def __init__(self, water=0, lactic_acid=0, calcium_lactate=0, glucose=0, bacteria=0,
                 csl_solids=0, tween80=0, octanol=0, temperature=0):
        self.Water = water
        self.LacticAcid = lactic_acid
        self.CalciumLactate = calcium_lactate
        self.Glucose = glucose
        self.Bacteria = bacteria
        self.CSLSolids = csl_solids
        self.Tween80 = tween80
        self.Octanol = octanol

        self.Temperature = temperature

        self.TotalMass = self.Water + self.LacticAcid + self.CalciumLactate + self.Glucose + \
                         self.Bacteria + self.CSLSolids + self.Tween80 + self.Octanol

        self.Volume = self.get_volume()

    def get_volume(self):
        water_volume = Chem.component_mass_to_volume(self.Water, 'Water')
        lactic_acid_volume = Chem.component_mass_to_volume(self.LacticAcid, 'Lactic Acid')
        calcium_lactate_volume = Chem.component_mass_to_volume(self.CalciumLactate, 'Calcium Lactate')
        glucose_volume = Chem.component_mass_to_volume(self.Glucose, 'Glucose')
        bacteria_volume = Chem.component_mass_to_volume(self.Bacteria, 'Bacteria')
        csl_solids_volume = Chem.component_mass_to_volume(self.CSLSolids, 'Corn Steep Liquor')
        tween80_volume = Chem.component_mass_to_volume(self.Tween80, 'Tween 80')
        octanol_volume = Chem.component_mass_to_volume(self.Octanol, 'Octanol')

        total_volume = water_volume + lactic_acid_volume + calcium_lactate_volume + glucose_volume + \
                       bacteria_volume + csl_solids_volume +  tween80_volume + octanol_volume

        return total_volume
