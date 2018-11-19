from Vehicle import Vehicle
from Solution import Solution


        
def EvolutiveAlgorithm(data, vehicle):
    solutions = []
    NumOfNodes = len(data.routeInfo)
    initial_Solution = Solution(NumOfNodes)
    initial_Solution.randomChoise()
    
    mutation = initial_Solution.isChargeNode
    initialPoblation = 100
    for individual in range(initialPoblation):
        feasibleIndividual = evaluatePath(data,mutation,vehicle)
        if(feasibleIndividual):
            solutions.append(mutation)
        vehicle = Vehicle()
        another_Solution = Solution(NumOfNodes)
        another_Solution.randomChoise()
        mutation = another_Solution.isChargeNode
    print()
    
def evaluatePath(data,choices,vehicle):
    for i in range (len(choices)-1):
        isSelectedNode = choices[i]
        node_index = i
        current_node = data.routeInfo[node_index]
        next_node = data.routeInfo[node_index+1]
        if isSelectedNode == 1:
            refuel_at_max(vehicle, current_node)
            drive(vehicle, current_node, next_node,data)
        else:
            drive(vehicle, current_node, next_node,data)
        
        if(not isFeasible(vehicle,next_node,len(choices)-1)):
            print("nojepudo")
            return False
    return True
    
def isFeasible(vehicle,next_node, size):
    of_route_condition = (vehicle.ofRouteCount <= vehicle.maxOutRoute)
    minFuelCondition = (vehicle.currentFuel >= vehicle.minfuelAnyTime_Gall)
    time_aceptance = (vehicle.time <= next_node.endWindow)
    last_node_criteria = True
    if(next_node.stopId == size):
        last_node_criteria = (vehicle.currentFuel >= vehicle.requiredFuelAtDest_Gall)
        
    return (of_route_condition and minFuelCondition and time_aceptance and last_node_criteria)
    
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
    

def refuel_at_max(vehicle, current_node):
    to_refuel = vehicle.tankCapacity_Gall - vehicle.currentFuel
    if to_refuel >= vehicle.minRefuelQuantity_Gall:
        
        offRoute_miles = current_node.oor
        if offRoute_miles > 0:
            vehicle.currentFuel -= ((offRoute_miles ** -1) * (vehicle.milesPerGallon)) ** -1
            vehicle.ofRouteCount += offRoute_miles
            
        to_refuel = vehicle.tankCapacity_Gall - vehicle.currentFuel
        price = (to_refuel * current_node.price)
        vehicle.currentFuel += to_refuel
        vehicle.acumulatePrice += price
        vehicle.time += offRoute_miles/vehicle.speed_mph