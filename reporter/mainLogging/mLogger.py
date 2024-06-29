# import logging.config
# Load configuration from file
# logging.config.fileConfig('logging_config.ini')

import logging
logging.basicConfig(filename='application.log', level=logging.DEBUG,format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S')