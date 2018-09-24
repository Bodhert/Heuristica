def canIArrive(vehicle,currentNode, nextNode):
    tempVehicle = vehicle
    milesTotravel = nextNode.cumMile - currentNode.cumMile
    currentFuel_gal = tempVehicle.currentFuel - ((milesTotravel**-1) *  tempVehicle.milesPerGallon )**-1 # converting unities
    print("hola")
    

def ConstructiveAlgorithm(data,vehicle, idStart, idEnd):
    current = idStart
    arrive = False
    while current != idEnd:
        currentNode = data.route[current]
        nextNode = data.route[current + 1]   
        current =current + 1
        canIArrive(vehicle, currentNode, nextNode)
    