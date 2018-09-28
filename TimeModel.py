import time

class TimeModel:

    def __init__(self, seconds_multiplier = 3600 * 24, model_years = 5):
        self.seconds_multiplier = seconds_multiplier
        self.model_years = model_years
        self.Running = False

    def start(self):
        if self.Running:
            print("Time is already running")
        else:
            self.start_model()

    def stop(self):
        if self.Running:
            self.Running = False
            print ("Time has been stopped")
        else:
            print ("Time is already stopped")

    def start_model(self):
        years = self.model_years
        seconds = years * 365 * 24 * 60
        model_seconds = seconds / self.seconds_multiplier
        now = time.time()
        future = now + model_seconds
        print("Time has been started")
        while time.time() < future:
            self.Running = True

        self.stop()
