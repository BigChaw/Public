import subprocess
import wmi
import os
import time

LIST_FILE_EXTENSION = [".LOG", ".log", ".html", ".py", ".pyc", ".txt", ".PNG", ".zip", ".mp3"]

SPLIT_TEXT = os.path.splitext
IS_FILE = os.path.isfile
IS_DIR = os.path.isdir
LIST_DIR = os.listdir
DIR_D = ("D:")
DIR_E = ("E:")
PATH_D = IS_DIR(f"{DIR_D}")
PATH_E = IS_DIR(f"{DIR_E}")
DEMAND_ELEMENT = "Windows D&D"

# Function for printout Table with Drives, Caption and check if Removable disk is detected or not --> z "Netu"
def check_connection_USB():
    global output
    output = subprocess.check_output("wmic logicaldisk get drivetype, caption \n", shell=True)
    for drive in str(output).strip().split("\\r\\r\\n"):
        if "2" in drive:
            drive_caption = drive.split()[0]
            drive_type = drive.split(":")[1].strip()
            if drive_type == "2":
                print(drive_caption + " is Removable disk")
    else:
        if "2" not in str(output):
            print("\nNo Removable disk is not connected. Please check connection of USB and try it again! \n")

def USB_information():
    im = wmi.WMI()
    
    # All information about given USBs
    for disk in im.Win32_LogicalDisk(DriveType=2):
        print(disk)

# Function for decting of USBs --> Inspirace z "Netu"
def USB_detecting():
    while True:
        if os.path.isdir('D:') and os.path.isdir('E:'):
            print("\nD: is connected... ") 
            print("E: is connected.. \n")
            break
        elif os.path.isdir('D:'):
            print("\nD: is connected... \n")
            break
        elif os.path.isdir('E:'):
            print("E: is connected... \n")
            break
        else:
            print("Detecting...")
            time.sleep(2)
        print("Waiting for connection of USB \n")
        
def listing_USB():  
    try:      
        while True:
            list_dir_d = (LIST_DIR (f"{DIR_D}"))
            for item in list_dir_d:
                time.sleep(1)
                if item == DEMAND_ELEMENT:
                    print(item + " --> This is correct folder")
                    break
                else:
                    if item != DEMAND_ELEMENT:
                        print(item)
            if DEMAND_ELEMENT in item:
                print(f"\nFolder with D&D found. You can use this USB!\n")
            else:
                print("\nFolder not found. Check other USB!")
            break
        
    except Exception:
        print(f"You have not connected USB at Driver {DIR_E}...\n")
           
# Still under working!!!
def file_extension():
    if PATH_D is True:       
        print(PATH_D)
    neco = os.listdir(DIR_D)
    print(neco)
    
    for item in neco:
        print(item)
    while True:
        if item.endswith(LIST_FILE_EXTENSION):
            print(item)
    
def main():
    USB_information()
    check_connection_USB()
    USB_detecting()
    listing_USB()
    #file_extension()
    #checktext()
main()    

