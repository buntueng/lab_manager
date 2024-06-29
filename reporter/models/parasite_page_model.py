"""model for parasite page"""
import logging
import mariadb
import yaml
import os

logger = logging.getLogger(__name__)
current_dir = os.path.dirname(__file__)
server_params = []
parasite_sql_cmds = []

# load server config file
yml_server_path = os.path.join(current_dir,"server_config.yml")

try:
    with open(yml_server_path,'r') as yml_file:
        server_params = yml_file.safe_load(yml_file)
except FileNotFoundError as e:
    logger.error("server_config.yml not found")
except Exception as e:
    logger.error(f"Error: {e}")

# Load parasite sql command from parasite_sql.yml
yml_path = os.path.join(current_dir, "parasite_sql.yml")

try:
    with open(yml_path, "r") as yml_file:
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



