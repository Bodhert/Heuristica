import csv
from Node import Node
from random import random

class Data:
#     route = [] #shared by all the instances, be careful
    
    def __init__(self):
        self.route = []
    
    def generateNoise(self):
        for i,tempNode in enumerate(self.route):
            value = random()
            tempNode.price = tempNode.price + value
            tempNode.cumMile = tempNode.cumMile + (value * ((tempNode.cumMile + 10) - tempNode.cumMile)) # dont want to go more then 10 miles 
            tempNode.oor =  tempNode.oor + (value * ((tempNode.oor + 10) - tempNode.oor))
            self.route[i] = tempNode
            
    def generateNoiseInValue(self,distortion):
        for i,tempNode in enumerate(self.route):
            value =  distortion * random()
            tempNode.price = tempNode.price + value
            tempNode.cumMile = tempNode.cumMile + (value * ((tempNode.cumMile + 10) - tempNode.cumMile)) # dont want to go more then 10 miles 
            tempNode.oor =  tempNode.oor + (value * ((tempNode.oor + 10) - tempNode.oor))
            self.route[i] = tempNode
    
    
    def saveRoute(self):
        with open('Data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                stopId = int(row["StopID"])
                price = float(row["Price"])
                acumulativeMiles = float(row["CumMile"])
                ofRoadMiles = float(row["OOR"])
                self.route.append(Node(stopId,price,acumulativeMiles,ofRoadMiles))
      
    def printDataFromFile(self):
        with open('Data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                print(f'\t{row["StopID"]}  {row["Price"]}  {row["CumMile"]} {row["OOR"]}.')
                line_count += 1
            print(f'Processed {line_count} lines.')
        