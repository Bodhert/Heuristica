from Data import Data
from Vehicle import Vehicle
from Methods import *
import time
from matplotlib.cbook import tostr
import time



def main():
    vehicle = Vehicle()
    data = Data()
    data.saveRoute()
    
    start_time = time.time()
    EvolutiveAlgorithm(data,vehicle)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
if __name__ == "__main__": main()