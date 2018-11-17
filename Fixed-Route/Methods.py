# refueling_nodes =[]
from Vehicle import Vehicle
import copy

def checkConditions(vehicle,currentNode, nextNode):
    tempVehicle = vehicle
    milesTotravel = nextNode.cumMile - currentNode.cumMile 
    if milesTotravel != 0.0:
        currentFuel_gal = tempVehicle.currentFuel - ((milesTotravel**-1) *  tempVehicle.milesPerGallon )**-1 # converting unities
        return currentFuel_gal >= tempVehicle.minfuelAnyTime_Gall
    return True

def checkIfFeasibleNeighborhood(List_Neigboorhood, vehicle):
    ofRoadRouteAcum = 0
    for node in List_Neigboorhood:
        ofRoadRouteAcum = ofRoadRouteAcum + node.oor
    
    return ofRoadRouteAcum <= vehicle.maxOutRoute 

def advance(vehicle,currentNode, nextNode):
    if currentNode.cumMile != nextNode.cumMile: # have to think well this question
        milesTotravel = nextNode.cumMile - currentNode.cumMile
        vehicle.currentFuel = vehicle.currentFuel - (((milesTotravel**-1) *  vehicle.milesPerGallon )**-1)
        
def AsapFuelPolicy(vehicle,currentNode):
    toRefuel = vehicle.tankCapacity_Gall - vehicle.currentFuel
    price = toRefuel * currentNode.price
    vehicle.currentFuel = vehicle.currentFuel +  toRefuel
    vehicle.acumulatePrice = vehicle.acumulatePrice + price  

def List_of_solutions_with_ConstructiveAlgorithm(data,vehicle, idStart, idEnd):
    current = idStart
    arrive = False
    refueling_nodes = []
    while current != idEnd:
        currentNode = data.route[current]
        nextNode = data.route[current + 1]
        current =current + 1
        if(checkConditions(vehicle, currentNode, nextNode)):
            advance(vehicle, currentNode, nextNode)
        else:
            AsapFuelPolicy(vehicle, currentNode)
            if(checkConditions(vehicle, currentNode, nextNode)):
                refueling_nodes.append(currentNode)
                advance(vehicle, currentNode, nextNode)
#             else:
#                 print("No Solution know :( sorry")
#     print("constructive algorithm")
#     print (vehicle.acumulatePrice)
    return refueling_nodes

def do_the_route_charging_at_fithyPercent(List_of_charging_points, vehicle):
    for station in List_of_charging_points:
        fuel_at_fithy_percent(station, vehicle)
        if len(List_of_charging_points) > 0:
            for i in range(0,len(List_of_charging_points)-1):
                advance(vehicle, List_of_charging_points[i],List_of_charging_points[i+1])

def fuel_at_fithy_percent(node, vehicle):
    midCharge = vehicle.tankCapacity_Gall - vehicle.minfuelAnyTime_Gall
    to_refuel = midCharge - vehicle.currentFuel 
    if to_refuel > 0:
        vehicle.acumulatePrice =  vehicle.acumulatePrice + (to_refuel*node.price)
        vehicle.currentFuel = vehicle.currentFuel + to_refuel
        
    

def NoiseAndConstruc(data,vehicle, idStart, idEnd):
    NoisedData = copy.copy(data)
    NoisedData.generateNoise()
    print("Noised Algorithm")
    List_of_solutions_with_ConstructiveAlgorithm(NoisedData,vehicle, idStart, idEnd)

def make_move_on_a_neighborhood(initial_neighborhood, data):
    if len(initial_neighborhood) > 0:
        next_neighborhood = []
        for node in initial_neighborhood:
            if node.stopId >= 5:
                alteration = data.route[node.stopId - 5]
                next_neighborhood.append(alteration)
        return next_neighborhood
    else:
        print("sorry no empty list allowed")
            

def make_move_on_a_neighborhood_adding_more_charging_points(list_inital_neighbohood, data):
    newNeigbor = list_inital_neighbohood[:]
    size = len(list_inital_neighbohood)
    for i in range(size):
        currentNode = list_inital_neighbohood[i]
        nextToInsert = data.route[currentNode.stopId]
        if i != size-1:
            newNeigbor.insert(i+1,nextToInsert)
        else:
            newNeigbor.insert(i,nextToInsert)
            
    return newNeigbor

def NoisyMethod(data,vehicle, idStart, idEnd):
    originalData = copy.copy(data)
    data.generateNoise()
    Best_Know_solution = List_of_solutions_with_ConstructiveAlgorithm(data,vehicle, idStart, idEnd)
    best_price = vehicle.acumulatePrice
    NoiseFactor = 100
    for i in range(0,100):
        vehicle_temp = Vehicle()
        data = originalData
        data.generateNoiseInValue(NoiseFactor)
        NoiseFactor = NoiseFactor-i
        temp_solution = List_of_solutions_with_ConstructiveAlgorithm(data,vehicle_temp, idStart, idEnd)
        if(vehicle.acumulatePrice < best_price):
            Best_Know_solution = temp_solution
            best_price = vehicle.acumulatePrice 
    vehicle.acumulatePrice = best_price
    