import uuid, random

from baseStructure import baseStructure
from config import dndTrackerConfig


class _tradeInitError(Exception):
    def __init__(self, message, location=None):
        super().__init__(message)
        self.location = location



class _tradeMakeError(Exception):
    def __init__(self, message):
        super().__init__(message)



class _tradeStructure(baseStructure):
    def __init__(self, name, location, num_trades: int = None, num_trades_min: int = None, num_trades_max: int = None, cost_modification: float = 1.0, num_trade_class_min: int = None, num_trade_class_max: int = None, trade_class_list: list = None):
        super().__init__(name, location)

        # number of trade class
        if not (num_trade_class_min and num_trade_class_max and trade_class_list):
            raise _tradeInitError('Trader must have a specified trade class or number of trade classes')
        elif (num_trade_class_min and num_trade_class_max) and trade_class_list:
            raise _tradeInitError('Only "trade_class_list" or "num_trade_class_min" and "num_trade_class_max" can be specified')
        elif (num_trade_class_min and not num_trade_class_max) or (num_trade_class_max and not num_trade_class_min):
            raise _tradeInitError('Both "num_trade_class_min" and "num_trade_class_max" must be specified')

        # number of trades
        if not (num_trades and num_trades_min and num_trades_max):
            raise _tradeInitError('Specify "num_trades" for a specific number of trades or "num_trades_min" and "num_trades_max" for a dynamic number of trades')
        elif num_trades and (num_trades_min and num_trades_max):
            raise _tradeInitError('Only "num_trades" or "num_trades_min" and "num_trades_max" can be specified')
        elif (num_trades_min and not num_trades_max) or (num_trades_max and not num_trades_min):
            raise _tradeInitError('Both "num_trades_min" and "num_trades_max" must be specified')

        # convert specified trade num to work
        if num_trades:
            num_trades_min = num_trades
            num_trades_max = num_trades
        
        self.cost_modification = cost_modification
        self.trade_class = []
        self.num_trades_min = num_trades_min
        self.num_trades_max = num_trades_max
        self.trades = {}
 
        ##############################
        # from somewhere get a class #
        #         aka make DB        #
        ##############################

        # get trade class(s)
        if trade_class_list:
            ###################
            # Add validation? #
            ###################
            self.trade_class = trade_class_list
        else:
            num_trade_class = random.randint(num_trade_class_min, num_trade_class_max)
            for trade_class in range(num_trade_class):
                # get trade class
                self.trade_class.append('<TRADE_CLASS>')
            
            #########################
            # MORE LOGIC TO PREVENT #
            #  DUPLICATE CLASSES??  #
            #  OR HAVE MORE TRADES  #
            #       PER CLASS       #
            #########################


    # update cost modification
    def change_cost_modification(self, cost_modification):
        self.cost_modification = cost_modification

                
    # when item is traded
    def make_trade(self, item: str, amount: int):
        # trade validation
        if item not in self.trades.items():
            raise _tradeMakeError(f'Item "{item}" is not avalible at this trade point')
        if int(amount) > int(self.trades[item]):
            raise _tradeMakeError(f'Trader point only has {self.trades[item]} {item}')
        
        # make trade
        self.trades[item] -= amount

        return f'Trade made for {amount} {item}, {self.trades[item]} left'


    # new trades (on init each time)
    def get_trades(self, quantity_min: int = 1, quantity_max: int = 5):
        # remove last trades
        self.clean_trades()

        # validation
        if self.trade_class == None:
            raise _tradeInitError('Trader must have a trade class')

        trades_avalible = random.randint(self.num_trades_min, self.num_trades_max)

        for trade in range(trades_avalible):
            #####################################
            # pull trades from databse          #
            # where trade class                 #
            # much db and other logic required? #
            #####################################
            trade = trade
            self.trades[trade] = random.randint(quantity_min, quantity_max)


    def clean_trades(self):
        self.trades = []



# stall 
class stall(_tradeStructure):
    def __init__(self, name, location, num_trades = None, num_trades_min = 1, num_trades_max = 10, cost_modification = 1, num_trade_class_min = 1, num_trade_class_max = 1, trade_class_list = None):
        # validation
        super().__init__(name, location, num_trades, num_trades_min, num_trades_max,  cost_modification, num_trade_class_min, num_trade_class_max, trade_class_list)



# shop
class shop(_tradeStructure):
    def __init__(self, name, location, num_trades = None, num_trades_min = 5, num_trades_max = 30, cost_modification = 1, num_trade_class_min = 1, num_trade_class_max = 5, trade_class_list = None):
        # validation?
        super().__init__(name, location, num_trades, num_trades_min, num_trades_max, cost_modification, num_trade_class_min, num_trade_class_max, trade_class_list)



# market (both)
class market(_tradeStructure):
    def __init__(self, name, location, num_trades = None, num_trades_min = 15, num_trades_max = 50, cost_modification = 1, num_trade_class_min = 20, num_trade_class_max = 50, trade_class_list = None):
        # validation?
        super().__init__(name, location, num_trades, num_trades_min, num_trades_max, cost_modification, num_trade_class_min, num_trade_class_max, trade_class_list)



# make trade structure example
def main(trade_struc_type = None):
    options = dndTrackerConfig()

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

    # init trade struct
    if trade_struc_type == 'stall':
        # all option
        final_struct = stall(
            name = uuid.uuid4(), 
            location = 'x,y?',
            num_trades_min = options.stall_trade_amount_min,
            num_trades_max = options.stall_trade_amount_max,
            cost_modification = 1,
            num_trade_class_min = options.stall_trade_class_min,
            num_trade_class_max = options.stall_trade_class_max,
            trade_class_list = None
        )
    elif trade_struc_type == 'shop':
        # use default
        final_struct = shop(
            name = uuid.uuid4(), 
            location = 'x,y?',
        )
    elif trade_struc_type == 'market':
        # use default
        final_struct = market(
            name = uuid.uuid4(), 
            location = 'x,y?',
        )

    # init trader (each time)
    final_struct.get_trades()

    # make trade 
    final_struct.make_trade(
        item = '<item-to-trade>',
        amount = '<amount-traded>'
        )

    # on 'unload'
    final_struct.clean_trades()