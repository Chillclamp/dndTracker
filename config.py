import os
from dotenv import load_dotenv

class dndTrackerConfig:
    def __init__(self):
        load_dotenv()

        self.host_ip = os.getenv("HOST_IP", "127.0.0.1")
        self.host_port = int(os.getenv("HOST_PORT", "80"))