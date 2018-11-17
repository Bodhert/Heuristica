
class Node:    
    def __init__(self, stopId, Price, CumMile, OOR, startWindow=-1, endWindow=-1):
        self.stopId = stopId
        self.price = Price
        self.cumMile = CumMile
        self.oor = OOR
        self.startWindow=startWindow
        self.endWindow=endWindow
        
