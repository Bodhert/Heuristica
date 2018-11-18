from Vehicle import Vehicle
from Solution import Solution
from jmespath.ast import current_node




def isFeasibleRoute(solution):
    return True

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
        
def EvolutiveAlgorithm(data, vehicle):
    NumOfNodes = len(data.routeInfo)
    initial_Solution = Solution(NumOfNodes)
    initial_Solution.randomChoise()
    mutation = initial_Solution.isChargeNode
    evaluatePath(data,mutation,vehicle);
    print()
    
def evaluatePath(data,choices,vehicle):
    for i in range (len(choices)-1):
        isSelectedNode = choices[i]
        node_index = i
        current_node = data.routeInfo[node_index]
        next_node = data.routeInfo[node_index+1]
        if isSelectedNode == 1:
            temp_data = data.routeInfo[node_index]
            #refuel
            drive(vehicle, current_node, next_node)
        else:
            drive(vehicle, current_node, next_node)
    
def drive(vehicle,current_node,next_node):
    miles_ahead = -1
    if current_node.stopId == 1 or current_node.cumMile ==  next_node.cumMile:
        miles_ahead = current_node.cumMile
    else:
        miles_ahead = next_node.cumMile - current_node.cumMile
    vehicle.currentFuel -= ((miles_ahead ** -1) * (vehicle.milesPerGallon)) ** -1
    vehicle.time += miles_ahead/vehicle.speed_mph
    
