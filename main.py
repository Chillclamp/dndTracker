
import os

import config
from webServer import webServer


def main(options: config.dndTrackerConfig):
    # Start webServer 
    os.chdir('webServer')
    web = webServer.start_server(options.host_ip, options.host_port)

if __name__ == '__main__':
    main(config.dndTrackerConfig())