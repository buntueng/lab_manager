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
        customer_name = keyword_search[0].text(0)
        customer_surname = keyword_search[0].text(1)
        result = []
        sql_cmd = self.sql_cmd["search_customer_case"]
        result = self.select_data(sql_cmd, [customer_name, customer_surname])
        return result

    def get_all_customer_names(self):
        """Get all customer names"""
        result = []
        sql_cmd = self.sql_cmd["get_all_customer_names"]
        result = self.select_data(sql_cmd, [])
        return result

    def new_case_search_customer(self, keyword_search):
        """Search customer case using customer name or surname"""
        result = []
        sql_cmd = self.sql_cmd["new_case_search_customer"]
        result = self.select_data(sql_cmd, [keyword_search, keyword_search])
        return result

    def save_new_customer(self, group_id, title, name, surname, tax_id,
                          email, line_id, phone, contact_address, bill_address, updater) -> bool:
        """Save new customer to the database"""
        sql_cmd = self.sql_cmd["insert_new_customer"]
        data = (group_id, title, name, surname, tax_id,
                email, line_id, phone, contact_address, bill_address, updater)
        if self.insert_data(sql_cmd, data):
            return True
        else:
            return False

    def save_case_register(self, row_list, updater) -> bool:
        """Save new case to the database"""
        print("save_case_register")
        return True

    def insert_data(self, sql_cmd, data) -> bool:
        """Insert data to the database"""
        try:
            conn = mariadb.connect(
                user=self.server_config["user"],
                password=self.server_config["password"],
                host=self.server_config["host"],
                port=self.server_config["port"],
                database=self.server_config["database"]
            )
            cur = conn.cursor()
            cur.execute(sql_cmd, data)
            conn.commit()
            conn.close()
            return True
        except mariadb.Error as e:
            QMessageBox.critical(None, "Error", f"Error: {e}")
            return False

    def get_last_case_number(self) -> str:
        """Get the last case number from the database"""
        sql_cmd = self.sql_cmd["get_last_case_number"]
        last_case_number = self.select_data(sql_cmd, [])
        return last_case_number[0][0]

    def save_new_case_register(self, case_data, updater) -> int:
        """Save case register to the database"""
        sql_cmd = self.sql_cmd["get_customer_id_from_name_and_tax"]
        sender_id = self.select_data(
            sql_cmd, [case_data[0], case_data[1], case_data[2]])[0][0]
        owner_id = self.select_data(
            sql_cmd, [case_data[3], case_data[4], case_data[5]])[0][0]
        sql_cmd = self.sql_cmd["insert_new_case"]
        case_data = [sender_id, owner_id, case_data[6], updater]
        current_id = self.insert_data_return_id(sql_cmd, case_data)
        return current_id

    def save_specimen_information(self, specimen_data) -> int:
        """Save specimen information"""
        sql_cmd = self.sql_cmd["insert_new_sample"]
        current_id = self.insert_data_return_id(sql_cmd, specimen_data)
        return current_id

    def insert_data_return_id(self, sql_cmd, data) -> int:
        """Insert data to the database"""
        try:
            conn = mariadb.connect(
                user=self.server_config["user"],
                password=self.server_config["password"],
                host=self.server_config["host"],
                port=self.server_config["port"],
                database=self.server_config["database"]
            )
            cur = conn.cursor()
            cur.execute(sql_cmd, data)
            cur.execute("SELECT LAST_INSERT_ID()")
            current_id = cur.fetchone()[0]
            conn.commit()
            conn.close()
            return current_id
        except mariadb.Error as e:
            QMessageBox.critical(None, "Error", f"Error: {e}")
            return 0

    def save_molecular_biology_information(self, sample_id, molecular_biology_data, updater) -> bool:
        """Save molecular biology information."""
        sql_cmd = self.sql_cmd["insert_new_molecular_biology_tests"]
        molecular_biology_data = [sample_id] + \
            molecular_biology_data + [updater]
        if self.insert_data(sql_cmd, molecular_biology_data):
            return True
        else:
            return False

    def save_parasite_information(self, sample_id, parasite_data, checkbox_state, updater) -> bool:
        """Save parasite information."""
        sql_cmd = self.sql_cmd["insert_new_parasite_biology_test"]
        reformat_data = []
        for i, cb_state in enumerate(checkbox_state):
            reformat_data.append(parasite_data[2*i])
            reformat_data.append(cb_state)
            reformat_data.append(parasite_data[2*i+1])
        data = [sample_id] + reformat_data + [updater]
        if self.insert_data(sql_cmd, data):
            return True
        else:
            return False

    def save_bacteria_lab_information(self, sample_id, bacteria_data, updater) -> bool:
        """Save bacteria lab information."""
        sql_cmd = self.sql_cmd["insert_new_bacteria_biology_test"]
        bacteria_data = [sample_id] + bacteria_data + [updater]
        if self.insert_data(sql_cmd, bacteria_data):
            return True
        else:
            return False

    def get_parasite_data(self, sample_id) -> list:
        """Get parasite data."""
        sql_cmd = self.sql_cmd["get_parasite_data"]
        data = self.select_data(sql_cmd, [sample_id])
        return data

    def save_lab_order(self, case_id, lab_id, comments, updater) -> bool:
        """Save lab order."""
        sql_cmd = self.sql_cmd["save_lab_order"]
        lab_order_data = [case_id, lab_id, comments, updater]
        if self.insert_data(sql_cmd, lab_order_data):
            return True
        else:
            return False

    def get_lab_order_details(self, case_id) -> list:
        """Get lab order details."""
        sql_cmd = self.sql_cmd["reload_case_detail"]
        data = self.select_data(sql_cmd, [case_id])
        return data

    def get_case_detail_by_customer_name(self, customer_name, customer_surname) -> list:
        """Get case detail by customer name."""
        sql_cmd = self.sql_cmd["get_case_detail_by_customer_name"]
        data = self.select_data(sql_cmd, [customer_name, customer_surname])
        return data

    def get_today_case_detail(self):
        """Get today case detail."""
        sql_cmd = self.sql_cmd["get_today_case_detail"]
        data = self.select_data(sql_cmd, [])
        return data

    def delete_specimen_in_new_case_page(self, sample_id) -> bool:
        """Delete specimen in new case page."""
        sql_cmd = self.sql_cmd["remove_case_detail"]
        if self.insert_data(sql_cmd, [sample_id]):
            return True
        else:
            return False

    def get_all_employee_detail(self) -> list:
        """Get all employee detail."""
        sql_cmd = self.sql_cmd["get_all_employee_detail"]
        data = self.select_data(sql_cmd, [])
        return data

    def save_tracking_information(self, barcode_id, employee_id, updater, tracking_info) -> bool:
        """Save lab received sample information."""
        sql_cmd = self.sql_cmd["save_lab_received_sample_information"]
        data = [barcode_id, employee_id, updater, tracking_info]
        if self.insert_data(sql_cmd, data):
            return True
        else:
            return False

    def get_job_detail_in_check_job_progress_page(self) -> list:
        """Get job detail in check job progress page."""
        sql_cmd = self.sql_cmd["get_job_detail_in_check_job_progress_page"]
        data = self.select_data(sql_cmd, [])
        return data

    def get_job_detail_in_check_job_progress_page_by_id(self, job_id) -> list:
        """Get job detail in check job progress page by date."""
        sql_cmd = self.sql_cmd["get_job_detail_in_check_job_progress_page_by_id"]
        data = self.select_data(sql_cmd, [job_id])
        return data

    def get_sample_information_by_id(self, case_id):
        """Get sample information by id."""
        cmd = self.sql_cmd["get_sample_data"]
        sample_data = self.select_data(cmd, [case_id])
        return sample_data

    def get_test_information_by_id(self, case_id):
        """Get test information by id."""
        cmd = self.sql_cmd["get_bacteria_biology_tests"]
        test_data = self.select_data(cmd, [case_id])
        return test_data
    
    def get_parasite_test_information_by_id(self, case_id):
        """Get test information by id."""
        cmd = self.sql_cmd["get_parasite_biology_tests"]
        test_data = self.select_data(cmd, [case_id])
        return test_data
    
    def get_bacteriology_test_information_by_id(self, case_id):
        """Get test information by id."""
        cmd = self.sql_cmd["get_bacteriology_biology_tests"]
        test_data = self.select_data(cmd, [case_id])
        return test_data
    
    def get_molecular_test_information_by_id(self, case_id):
        """Get test information by id."""
        cmd = self.sql_cmd["get_molecular_biology_tests"]
        test_data = self.select_data(cmd, [case_id])
        return test_data
