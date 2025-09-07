import os
from dotenv import load_dotenv

from logger import dndLogger

class dndTrackerConfig:
    def __init__(self):
        load_dotenv()

        self.logger = dndLogger(log_to_file = True)

        ###         ACCESS CONFIG            ##
        self.host_ip = os.getenv("HOST_IP", "127.0.0.1")
        self.host_port = int(os.getenv("HOST_PORT", "80"))

        ###         TRADE OPTIONS            ###
        # stall
        self.stall_trade_amount_min = os.getenv("")
        self.stall_trade_amount_max = os.getenv("")
        self.stall_trade_class_min = os.getenv("")
        self.stall_trade_class_max = os.getenv("")

        # shop
        self.shop_trade_amount_min = os.getenv("")
        self.shop_trade_amount_max = os.getenv("")
        self.shop_trade_class_min = os.getenv("")
        self.shop_trade_class_max = os.getenv("")

        # market
        self.market_trade_amount_min = os.getenv("")
        self.market_trade_amount_max = os.getenv("")
        self.market_trade_class_min = os.getenv("")
        self.market_trade_class_max = os.getenv("")