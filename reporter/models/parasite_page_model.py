"""model for parasite page"""
import logging
import mariadb
import yaml
import os
import sys

logger = logging.getLogger(__name__)
server_params = []
parasite_sql_cmds = []



base_path = None
if getattr(sys, 'frozen', False):  # Check if running in a PyInstaller bundle
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)  # Use the current directory as the base path

# load server config file
yml_server_path = os.path.join(base_path,"server_config.yml")

try:
    with open(yml_server_path,'r', encoding='UTF8') as yml_file:
        server_params = yaml.safe_load(yml_file)
except FileNotFoundError as e:
    logger.error("server_config.yml not found")
except Exception as e:
    logger.error(f"Error: {e}")

# Load parasite sql command from parasite_sql.yml
yml_path = os.path.join(base_path, "parasite_sql.yml")

try:
    with open(yml_path, "r", encoding='UTF8') as yml_file:
        parasite_sql_cmds = yaml.safe_load(yml_file)
except FileNotFoundError as e:
    logger.error("parasite_sql.yml not found")
except Exception as e:
    logger.error(f"Error: {e}")


def save_parasite_data(data) -> bool:
    """ Save parasite data """
    sql_cmd = parasite_sql_cmds["save_parasite_report"]
    # connect database
    
    return True

def insert_database(sql_cmd,data) -> bool:
    """ Insert data to database """
    # connect database
    db = mariadb.connect(
        user=server_params["user"],
        password=server_params["password"],
        host=server_params["host"],
        port=server_params["port"],
        database=server_params["database"]
    )
    cursor = db.cursor()
    try:
        cursor.execute(sql_cmd, data)
        db.commit()
    except mariadb.Error as e:
        logger.error(f"Error: {e}")
        db.rollback()
        return False
    finally:
        cursor.close()
        db.close()
    return True



