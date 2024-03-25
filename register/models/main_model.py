"""Main Controller class"""
import os
import sys
import yaml
import time
import mariadb
from PySide6.QtWidgets import QMessageBox


class Main_Model:
    """Main Model class"""

    def __init__(self):
        self.model = None
        # if run from script then the path is the current directory. If run from exe then the path is the path to the exe
        config_path = None
        if getattr(sys, 'frozen', False):
            config_path = os.path.dirname(sys.executable)
        elif __file__:
            config_path = os.path.dirname(__file__)

        # read sql commands from the yaml file
        self.sql_cmd = None
        sql_yml_path = os.path.join(config_path, "sql_cmd.yml")
        with open(sql_yml_path, "r", encoding='UTF8') as file:
            self.sql_cmd = yaml.safe_load(file)

        # read server config from the server_config.yml file
        self.server_config = None
        server_config_path = os.path.join(
            config_path, "server_config.yml")
        with open(server_config_path, "r", encoding='UTF8') as file:
            self.server_config = yaml.safe_load(file)

    def search_today_sticker(self):
        # select all data from the database in table employee where the date is equal to the current date
        sql_cmd = self.sql_cmd["search_today_sticker"]
        # get current date. Data format is "dd-mm-yyyy"
        other_params = ""
        today_sticker = self.select_data(sql_cmd, other_params)
        # today_sticker = [["24-03-2024 10:00:00", "660000000001", "Avine",
        #                  "D304(BAC)", "ไม่แช่เย็น (Chill)", "ด่วนที่สุด", "หมายเหตุ"]]
        return today_sticker

    def user_sign_in(self, username, password):
        # select user_info from the database in talbe employee where username and password are equal to the given username and password
        sql_cmd = self.sql_cmd["user_sign_in"]
        data = (username, password)
        login_info = self.select_login_data(sql_cmd, data)
        return login_info

    def select_data(self, sql_cmd, info) -> list:
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
            cur.execute(sql_cmd, info)
            data = cur.fetchall()
            conn.close()
            return data
        except mariadb.Error as e:
            QMessageBox.critical(None, "Error", f"Error: {e}")
            return []

    def select_login_data(self, sql_cmd, data) -> list:
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
            (user_username, user_password) = data
            cur.execute(sql_cmd, (user_username, user_password, True))
            data = cur.fetchall()
            conn.close()
            return data
        except mariadb.Error as e:
            QMessageBox.critical(None, "Error", f"Error: {e}")
            return []

    def search_customer_case(self, keyword_search):
        """Search customer case using customer name or surname"""
        result = []
        sql_cmd = self.sql_cmd["search_customer_case"]
        result = self.select_data(sql_cmd, keyword_search)
        return result
