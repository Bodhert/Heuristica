from Data import Data
from Vehicle import Vehicle
from Methods import *
import time
from matplotlib.cbook import tostr


def main():
    v = Vehicle()
    v2 = Vehicle()
    d = Data()
    d.saveRoute()
    
    #first method
    print("first method only constructive")
    start = time.time()
    List_of_solutions_with_ConstructiveAlgorithm(d, v, 1, 30)
    end = time.time()
    print (str(v.acumulatePrice) + "$")
    print("elapsed time " + str( end - start))
    print()
    
    #second method
    print("second method random in the data")
    start = time.time()
    NoiseAndConstruc(d, v2, 1, 30)
    end = time.time()
    print (str(v2.acumulatePrice) + "$")
    print("elapsed time " + str( end - start))
    
    #firstNeigborhood method
    print()
    print("First Neigborhood method")
    start = time.time()
    vehicle_3 = Vehicle()
    vehicle_3_1 = Vehicle()
    data_3 = Data()
    data_3.saveRoute()
    initial_neighbor = List_of_solutions_with_ConstructiveAlgorithm(data_3,vehicle_3,1,30)
    second_neighbor = make_move_on_a_neighborhood(initial_neighbor, data_3)
    do_the_route_charging_at_fithyPercent(second_neighbor, vehicle_3_1)
    print(str(vehicle_3_1.acumulatePrice) + "$")
    end = time.time()
    print("elapsed time " + str( end - start))
    
    #SecondNeigborhood method:
    print()
    print("second Neigborhood method")
    start = time.time()
    vehicle_4 = Vehicle()
    data_4 = Data()
    data_4.saveRoute()
    firstNeighborhood = List_of_solutions_with_ConstructiveAlgorithm(data_4,vehicle_4,1,30)
    secondNeighborhood = make_move_on_a_neighborhood_adding_more_charging_points(firstNeighborhood,data_4)
    if checkIfFeasibleNeighborhood(secondNeighborhood, vehicle_4):
        do_the_route_charging_at_fithyPercent(secondNeighborhood, vehicle_4)
        print(str(vehicle_4.acumulatePrice) + "$")
    else:
        print("not feasible neirboohood")
    end = time.time()
    print("elapsed time " + str( end - start))
    
    #Noising method (based on a local search)
    print()
    print("Noising method (based on a local search)")
    start = time.time()
    vehicle_5 = Vehicle()
    data_5 = Data()
    data_5.saveRoute()
    list_of_solution_nodes_5 = List_of_solutions_with_ConstructiveAlgorithm(data_5, vehicle_5, 1, 100)
    NewCost = NoisyMethod(data_5, vehicle_5, 1, 30)
    print(str(vehicle_5.acumulatePrice) + "$")
    end = time.time()
    print("elapsed time " + str( end - start))
   
    
    
    
if __name__ == "__main__": main()