import csv
from Node import Node

class Data:
    route = []
      
    def saveRoute(self):
        with open('Data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.route.append(Node(1,2,3,4))
      
    def printData(self):
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
        