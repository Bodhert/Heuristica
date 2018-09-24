def checkConditions(vehicle,currentNode, nextNode):
    tempVehicle = vehicle
    milesTotravel = nextNode.cumMile - currentNode.cumMile 
    if milesTotravel != 0.0:
        currentFuel_gal = tempVehicle.currentFuel - ((milesTotravel**-1) *  tempVehicle.milesPerGallon )**-1 # converting unities
        return currentFuel_gal >= tempVehicle.minfuelAnyTime_Gall
    return True

def advance(vehicle,currentNode, nextNode):
    if currentNode.cumMile != nextNode.cumMile: # have to think well this question
        milesTotravel = nextNode.cumMile - currentNode.cumMile
        vehicle.currentFuel = vehicle.currentFuel - (((milesTotravel**-1) *  vehicle.milesPerGallon )**-1)
        
def AsapFuelPolicy(vehicle,currentNode):
    toRefuel = vehicle.tankCapacity_Gall - vehicle.currentFuel
    price = toRefuel * currentNode.price
    vehicle.currentFuel = vehicle.currentFuel +  toRefuel
    vehicle.acumulatePrice = vehicle.acumulatePrice + price  
    

def ConstructiveAlgorithm(data,vehicle, idStart, idEnd):
    current = idStart
    arrive = False
    while current != idEnd:
        currentNode = data.route[current]
        nextNode = data.route[current + 1]
        current =current + 1
        if(checkConditions(vehicle, currentNode, nextNode)):
            advance(vehicle, currentNode, nextNode)
        else:
            AsapFuelPolicy(vehicle, currentNode)
            if(checkConditions(vehicle, currentNode, nextNode)):
                advance(vehicle, currentNode, nextNode)
            else:
                print("No Solution know :( sorry")
    print("constructive algorithm")
    print (vehicle.acumulatePrice)
    
def NoiseAndConstruc(data,vehicle, idStart, idEnd):
    NoisedData = data
    NoisedData.generateNoise()
    print("Noised Algorithm")
    ConstructiveAlgorithm(NoisedData,vehicle, idStart, idEnd)
    

    