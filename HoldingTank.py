import FermentationMassBalance as FMB
import FluidStream as FS


class HoldingTank:

    def __init__(self):
        self.Volume = 0
        self.TotalMass = 0
        self.InFlow = FS.FluidStream()
        self.OutFlow = FS.FluidStream()
        self.InputStatus = False
        self.OutputStatus = False
