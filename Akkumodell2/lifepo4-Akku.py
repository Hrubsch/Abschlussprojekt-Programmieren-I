import numpy as np
from battery_pack_start import BatteryPack

class lifepo(BatteryPack): 
    def __init__(
        self,
        capacity_nom_cell_Ah : float = 10,
        initial_soc: float = 1.0,
        anz_parallel = 2,
  
    ):
        super().__init__( capacity_nom_cell_Ah, initial_soc, anz_parallel)
        self.internal_resistance_cell_mOhm = 8
        self.internal_resistance_pack_mOhm = self.anz_serie * self.internal_resistance_cell_mOhm / self.anz_parallel
        self.internal_resistance_pack_Ohm = self.internal_resistance_pack_mOhm  /1000 # mOhm in Ohm
        self.soc_array = np.array([0.00, 0.04, 0.09, 0.13, 0.17, 0.21, 0.26, 0.30, 0.40, 0.52, 0.64, 0.76, 0.88, 1.00])
        self.uoc_array = np.array([32.00, 35.87, 36.85, 37.56, 37.87, 38.28, 38.81, 39.05, 39.55, 40.27, 40.70, 41.16, 41.65, 42.00])

    def uoc(self) -> float:
        return np.interp(self.soc, self.soc_array, self.uoc_array)
    
class nmc(BatteryPack): 
    def __init__(
        self,
        capacity_nom_cell_Ah : float = 10,
        initial_soc: float = 1.0,
        anz_parallel = 2,
  
    ):
        super().__init__( capacity_nom_cell_Ah, initial_soc, anz_parallel)
        self.internal_resistance_cell_mOhm = 7
        self.internal_resistance_pack_mOhm = self.anz_serie * self.internal_resistance_cell_mOhm / self.anz_parallel
        self.internal_resistance_pack_Ohm = self.internal_resistance_pack_mOhm  /1000 # mOhm in Ohm
        self.soc_array = np.array([0.00, 0.04, 0.09, 0.13, 0.17, 0.21, 0.26, 0.30, 0.40, 0.52, 0.64, 0.76, 0.88, 1.00])
        self.uoc_array = np.array([32.00, 32.61, 33.17, 33.85, 34.24, 34.66, 35.39, 35.65, 36.65, 37.64, 38.91, 40.14, 41.08, 42.00])

    def uoc(self) -> float:
        return np.interp(self.soc, self.soc_array, self.uoc_array)
    

if __name__ == "__main__":
    b1 = BatteryPack(10.0)
    b2 = lifepo(10.0)

    print(b1)
    print(b2)

    b1.apply_current(10,120)
    b2.apply_current(10,120)

    print(b1)
    print(b2)
    
    batteries = [b1,b2]

    for b in batteries:
        print(b)
        b.apply_current(10,120)
        print(b)