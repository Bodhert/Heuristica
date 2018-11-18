class Vehicle:
    def __init__(self): # Default susuki parameters
        self.milesPerGallon = 6.00
        self.maxOutRoute = 3.00
        self.minRefuelQuantity_Gall= 50
        self.minfuelAnyTime_Gall = 40
        self.tankCapacity_Gall = 200
        self.initialFuel_Gall = 100
        self.requiredFuelAtDest_Gall = 100
        
        self.acumulatePrice = 0
        self.time = 0
        self.currentFuel = self.initialFuel_Gall
        self.speed_mph = 85 #mph