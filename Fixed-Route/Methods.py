from Vehicle import Vehicle
from Solution import Solution
import copy


        
def EvolutiveAlgorithm(data, vehicle):
    poblation = []
    NumOfNodes = len(data.routeInfo)
    
    initialPoblation = 100
    for individual in range(initialPoblation):
        individual_solution = Solution(NumOfNodes)
        individual_solution.randomChoise()
        vehicle = Vehicle()
        mutation = individual_solution.isChargeNode
        feasibleIndividual = evaluatePath(data,mutation,vehicle)
        if(feasibleIndividual):
            individual_solution.price = vehicle.acumulatePrice 
            poblation.append(individual_solution)
            
    
    for individual in poblation:
        local_search(individual,data)
    
    poblation.sort(key=lambda x: x.price, reverse=False)
    
    i = 0
    for solution in poblation:
        print(i)
        print(solution.price)
        i+=1
        
def local_search(individual,data):
    choices =  copy.deepcopy(individual.isChargeNode)
    size_of_array = len(choices) 
    for i in range(size_of_array-1):
        if(choices[i] == 1):
            if(i > 0 and choices[i-1] == 1):
                choices[i-1] = 0
            if(i < size_of_array and choices[i+1] == 1):
                choices[i+1] = 0
                
    vehicle = Vehicle()
    if(evaluatePath(data, choices, vehicle)):
        if(vehicle.acumulatePrice < individual.price):
            individual.isChargeNode = choices
            individual.price = vehicle.acumulatePrice 
    
    
    
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