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
            #refuel
            drive(vehicle, current_node, next_node,data)
        else:
            drive(vehicle, current_node, next_node,data)
    
    
def drive(vehicle,current_node,next_node,data):
    miles_ahead = -1
    if current_node.cumMile ==  next_node.cumMile:
        last_cum_mile = findLastDifferentMile(current_node, data)
        miles_ahead = current_node.cumMile - last_cum_mile
    else:    
        miles_ahead = next_node.cumMile - current_node.cumMile

    
    vehicle.currentFuel -= ((miles_ahead ** -1) * (vehicle.milesPerGallon)) ** -1
    vehicle.time += miles_ahead/vehicle.speed_mph

def findLastDifferentMile(current_node, data):
    last_index = current_node.stopId-1
    current_cumMiles = current_node.cumMile
    for i in range (last_index,-1,-1):
        previous_Mile = data.routeInfo[i].cumMile
        if current_cumMiles != previous_Mile:
            return previous_Mile
    return -1
    

def refuel(vehicle, current_node):
    print()
    
