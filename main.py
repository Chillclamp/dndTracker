
import os

import config
from webServer import webServer


def main(dndTrackerConfig: config.dndTrackerConfig):
    # Start webServer 
    os.chdir('webServer')
    web = webServer.start_server(dndTrackerConfig.host_ip, dndTrackerConfig.host_port)

if __name__ == '__main__':
    main(config.dndTrackerConfig())