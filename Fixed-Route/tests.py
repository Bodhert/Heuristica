import unittest
from Data import Data
from Vehicle import Vehicle
from Methods import *
from helloworld import *
from astropy.units import second

class TestForMethods(unittest.TestCase):
    
    def test_generate_charge_points_solutions(self):
        vehicle = Vehicle()
        data = Data()
        data.saveRoute()
        self.assertGreater(len(List_of_solutions_with_ConstructiveAlgorithm(data,vehicle,1,100)),0)
        
    def test_generate_neighborhood(self):
        vehicle = Vehicle()
        data = Data()
        data.saveRoute()
        firstNeighborhood = List_of_solutions_with_ConstructiveAlgorithm(data,vehicle,1,100)
        secondNeighborhood = make_move_on_a_neighborhood(firstNeighborhood,data)
        self.assertGreater(len(secondNeighborhood), 0)
        self.assertNotEqual(firstNeighborhood, secondNeighborhood)
    
    def test_feasible_neighborhood(self):
        vehicle = Vehicle()
        data = Data()
        data.saveRoute()
        firstNeighborhood = List_of_solutions_with_ConstructiveAlgorithm(data,vehicle,1,100)
        secondNeighborhood = make_move_on_a_neighborhood(firstNeighborhood,data)
        self.assertTrue(checkIfFeasibleNeighborhood(secondNeighborhood,vehicle))
        
    def test_cost_of_the_route(self):
        vehicle = Vehicle()
        data = Data()
        data.saveRoute()
        List_of_solution_nodes = List_of_solutions_with_ConstructiveAlgorithm(data, vehicle, 1, 400)
        do_the_route_charging_at_fithyPercent(List_of_solution_nodes,vehicle)
        self.assertNotEquals(vehicle.acumulatePrice,0)
        
    def test_fithyPercentCharge(self):
        vehicle = Vehicle()
        data = Data()
        data.saveRoute()
        List_of_solution_nodes = List_of_solutions_with_ConstructiveAlgorithm(data, vehicle, 1, 400)
        fuel_at_fithy_percent(List_of_solution_nodes[4], vehicle)
        self.assertAlmostEqual(vehicle.currentFuel, 160)
        