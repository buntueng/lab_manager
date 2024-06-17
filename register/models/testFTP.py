from ftplib import FTP, error_perm, all_errors
import socket
import yaml
import os

def download_png_from_ftp(ftp_server, ftp_user, ftp_password, file_path, local_file, use_passive=True):
    try:
        # Connect to the FTP server
        ftp = FTP()
        ftp.connect(ftp_server, 21, timeout=30)  # Adding a timeout
        ftp.login(user=ftp_user, passwd=ftp_password)
        print("Connected to the FTP server.")
        
        # Enable or disable passive mode
        ftp.set_pasv(use_passive)
        
        # Navigate to the directory containing the file
        file_directory = '/'.join(file_path.split('/')[:-1])
        file_name = file_path.split('/')[-1]
        
        if file_directory:
            try:
                ftp.cwd(file_directory)
                print(f"Changed directory to {file_directory}.")
            except error_perm as e:
                print(f"Failed to change directory: {e}")
                ftp.quit()
                return
        
        # Open a local file for writing in binary mode
        with open(local_file, 'wb') as f:
            try:
                # Use FTP's RETR command to download the file
                ftp.retrbinary(f'RETR {file_name}', f.write)
                print(f"File '{local_file}' downloaded successfully.")
            except error_perm as e:
                print(f"Failed to download file: {e}")
        
        # Close the FTP connection
        ftp.quit()
    except socket.timeout:
        print("Connection timed out.")
    except socket.error as e:
        print(f"Socket error: {e}")
    except all_errors as e:
        print(f"FTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    
ftp_server = ""
ftp_user = ""
ftp_password = ""
# load parameters from server_config.yml file
server_config_path = os.path.join(os.path.dirname(__file__), 'server_config.yml')
with open(server_config_path, "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    ftp_server = cfg["ftp_server"]
    ftp_user = cfg["ftp_user"]
    ftp_password = cfg["ftp_password"]


# Call the function to download the file
file_path = os.path.join("home","cvdtt","user_info","signature","01052024_155420.png")
local_file = os.path.join(os.path.dirname(__file__),"BT.png")
download_png_from_ftp(ftp_server, ftp_user, ftp_password, file_path, local_file)