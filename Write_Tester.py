import os
import subprocess
import errno

""" This code is for map network drive in my Job """


# Function for check of current disk - should be install with image!!!
def check_disk():
    if os.path.exists("C:\\"):
        print("Path exist for disk C.")
    if os.path.exists("D:\\"):
        print("Path exist for disk D.")
    else:
        print("Path does not exist!")
check_disk()

def map_network_drive(drive_letter: str, network_path: str, username: str, password: str) -> bool:
    
    try:
        # Constructing the command to map the network drive
        command = f'net use {drive_letter} {network_path} /user:{username} {password}'
 
        # Running the command using subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
 
        # Checking the output of the
        if result.returncode == 0:
            return True  # Network drive mapping successful
        else:
            return False  # Network drive mapping failed
 
    except Exception as c:
            print(f"Error occurred while mapping network drive: {c}")
            return False

drive_letter = 'Z:'
network_path = r'\\192.168.1.99\Data'
username = 'Emanuel'
password = 'Hashtag69'
 
success = map_network_drive(drive_letter, network_path, username, password)
 
if success:
    print(f"Network drive {drive_letter} mapped successfully.")
else:
    print(f"Failed to map network drive {drive_letter} or network drive is already mapped!")

map_network_drive(drive_letter, network_path, username, password)

# Function for make directories (C: and D:)
def mkdir():
    os.chdir(r"C:\Program files")
    try: 
        dir_make = os.mkdir(r"Write_Tester_Folder")
        
    except OSError as e:
        if e.errno == errno.EEXIST:
            print("Directory not created! Seems it is already created!")
        else:
            raise
    else: 
        print(f"Directory for C: driver is succesfully created!")
        
    os.chdir(r"D:") 
    try:
        os.mkdir(r"Write_Tester_Folder")
    except OSError as e:
        if e.errno == errno.EEXIST:
            print("Directory not created! Seems it is already created!")
        else:
            raise
    else: 
        print(f"Directory for D: driver is succesfully created!")
mkdir()
   