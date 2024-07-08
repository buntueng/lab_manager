import mariadb
import logging
import os
import yaml
import sys

class ReportModel:
    """ Class to handle the model of the application."""
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.current_user = []
        # load database configuration
        self.db_config = self._load_yaml_file("server_config.yml")
        self.sql_cmd = self._load_yaml_file("sql_cmd.yml")
        

    def _load_yaml_file(self, file_name):
        base_path = None
        if getattr(sys, 'frozen', False):
            print(sys._MEIPASS)
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)  # Use the current directory as the base path
        
        try:
            yaml_file_path = os.path.join(base_path, file_name)
            with open(yaml_file_path, "r", encoding='UTF8') as file:
                return yaml.safe_load(file)
        except (FileNotFoundError, yaml.YAMLError) as e:
            self.logger.error(f"Error loading YAML file '{file_name}': {e}")
            return None  # or raise an exception, depending on your nee

    def check_login(self, username, password) -> list:
        """ Method to check user login. """
        rows = []
        try:
            conn = mariadb.connect(host=self.db_config["database_ip"],
                                   port=self.db_config["database_port"],
                                   user=self.db_config["database_username"],
                                   password=self.db_config["database_password"],
                                   database=self.db_config["database_name"])
            cur = conn.cursor()
            cmd = self.sql_cmd["check_login"]
            cur.execute(cmd, [username, password])
            rows = cur.fetchall()
            conn.close()
        except mariadb.Error as e:
            logging.error(f"Error connecting to MariaDB Platform: {e}")
        return rows
