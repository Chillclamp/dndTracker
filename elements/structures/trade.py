import random


from baseStructure import baseStructure

class tradeInitError(Exception):
    def __init__(self, message, location=None):
        super().__init__(message)
        self.location = location


class tradeStructure(baseStructure):
    def __init__(self, name, location, cost_modification: float = 1.0,):
        super().__init__(name, location)
        
        self.cost_modification = cost_modification
        self.trade_class = None
        self.trades = []

    def make_trade(self, item, amount): 
        # in sel.trade take amount of item off
        # error if more trade than possible
        pass

                
# stall 
class stall(tradeStructure):
    def __init__(self, name, location, cost_modification = 1):
        super().__init__(name, location, cost_modification)

    def get_trade_class(self):
        # from somewhere get a class
        # possibly percent based
        pass
    
    def get_trades(self, number: int = 0):
        # validation
        if self.trade_class == None:
            raise tradeInitError('Trader must have a trade class')
        if number == 0:
            raise tradeInitError('Trader must be given a number of trades')
        
        for trade in range(number):
            # pull trades from databse
            # where trade class
            trade = trade
            self.trades.append(trade)


    


# shop

# market (both)




# make stall example
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

