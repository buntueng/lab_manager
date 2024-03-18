"""Main Controller class"""
import os
import yaml
import mariadb
from PySide6.QtWidgets import QMessageBox


class Main_Model:
    """Main Model class"""

    def __init__(self):
        self.model = None
        # read sql commands from the yaml file
        self.sql_cmd = None
        sql_yml_path = os.path.join(os.path.dirname(__file__), "sql_cmd.yml")
        with open(sql_yml_path, "r", encoding='UTF8') as file:
            self.sql_cmd = yaml.safe_load(file)

        # read server config from the server_config.yml file
        self.server_config = None
        server_config_path = os.path.join(
            os.path.dirname(__file__), "server_config.yml")
        with open(server_config_path, "r", encoding='UTF8') as file:
            self.server_config = yaml.safe_load(file)

    def user_sign_in(self, username, password):
        # select user_info from the database in talbe employee where username and password are equal to the given username and password
        sql_cmd = self.sql_cmd["user_sign_in"]
        data = (username, password)
        login_info = self.select_data(sql_cmd, data)
        return login_info

    def select_data(self, sql_cmd, data) -> list:
        """Select data from the database"""
        try:
            conn = mariadb.connect(
                user=self.server_config["user"],
                password=self.server_config["password"],
                host=self.server_config["host"],
                port=self.server_config["port"],
                database=self.server_config["database"]
            )
            cur = conn.cursor()
            (user_username,user_password) = data
            cur.execute(sql_cmd, (user_username,user_password, True))
            data = cur.fetchall()
            conn.close()
            return data
        except mariadb.Error as e:
            QMessageBox.critical(None, "Error", f"Error: {e}")
            return []
