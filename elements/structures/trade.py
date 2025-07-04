import random
from baseStructure import baseStructure

class tradeStructure(baseStructure):
    def __init__(self, name, location, materials, cost_modification: float = 1.0,):
        super().__init__(name, location, materials)
        
        self.cost_modification = cost_modification
        self.name = name
        self.location = location
        self.materials = materials
        
# stall 

class stall(tradeStructure):
    def __init__(self, name, location, materials, cost_modification = 1):
        super().__init__(name, location, materials, cost_modification)
    
    def get_trades(self):
        if self.trade_ckass == None:
            
            pass
        
        

# shop

class shop(tradeStructure):
    def __init__(self, name, location, materials, type):
        super().__init__(name, location, materials, type)

# market (both)

class market(tradeStructure):
    def __init__(self, name, location, materials, type):
        super().__init__(name, location, materials, type)

def main():
    
    # make struct logic
    
    final_struct = None
    
    # if not defined, set trade type
        
    if trade_struc_type == None:
        struct_type_chance = random.randint(1, 100)
        if struct_type_chance < 50:
            trade_struc_type = 'stall'
        elif struct_type_chance < 90:
            trade_struc_type = 'shop'
        elif struct_type_chance < 100:
            trade_struc_type = 'market'
        else:
            trade_struc_type = 'abandoned'
        
    
    self.trade_struc_type = trade_struc_type

    pass

