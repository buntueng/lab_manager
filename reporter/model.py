import mariadb
import logging.config
import logging
import os
import yaml


class ReportModel:

    def __init__(self):
        self.current_user = []
        config_file = os.path.join(os.path.dirname(
            __file__), "config_files", "log_config.ini")
        logging.config.fileConfig(config_file)  # load logging configuration
        self.logger = logging.getLogger('sLogger')
        self.logger.debug("Creating ReportModel object")

        # load database configuration
        self.db_config = self.load_yaml_file("config.yml")
        if self.db_config is None:
            self.logger.error("Database configuration file not loaded")
        else:
            self.logger.debug(f"Database configuration: {self.db_config}")

    def connect_to_database(self):
        self.logger.debug("Connecting to database")

    def check_login(self, username, password):
        self.logger.debug("Checking login")
        current_user = []   # get infomation from database

    def load_yaml_file(self, file_name):
        """ Method to load yaml file. """
        # set yaml file path
        data = None
        yaml_file_path = os.path.join(
            os.path.dirname(__file__), "config_files", file_name)
        try:
            with open(yaml_file_path, "r", encoding='UTF8') as file:
                data = yaml.safe_load(file)
                return data
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Error: {e}")
            return None
