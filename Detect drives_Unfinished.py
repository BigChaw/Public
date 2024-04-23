import subprocess
from tabulate import tabulate
import time
import re
import sys
import time

"""First must install library 'tabulate', 're', 'keyboard' --> not necessary"""

OUTPUT_GET_DRIVE: str = subprocess.check_output("wmic logicaldisk get drivetype, caption \n", shell=True)

# Type in function --> Still under working
""" def type_in():
    print("Wanna help?") """


# Print out table for understanding of which number means what
def table() -> str:
    # Specified the "drivetype" and different values:  
    table = [ 
        ["0", "Unknown"],
        ["1", "No root directory"],
        ["2", "Removable disk"],
        ["3", "Local disk"],
        ["4", "Network drive"],
        ["5", "Comapct disk"],
        ["6", "RAM disk"]
        ]
    
    # Header for table
    head: list = ["Value", "Meaning"]

    # Displayed table what is what for 
    global call_table
    call_table = tabulate(table, headers=head, tablefmt="simple_grid", numalign="Center")

# Function for if you want call table with Drives, Caption
def input_for_table() -> str:
    yes: list = ["Y","y"]
    no: list = ["n","N"]
    try:
        while True:
            choice: str = input(str("Wanna check the table for more information about drivers? (y/n)? "))
            if choice in yes:
                print(call_table)
            elif choice in no:
                break   
            else:
                sys.stdout.write("Please enter only: 'y/Y' or 'n/N'\n") 
                
    except Exception: 
        sys.stdout.write("Please enter only: 'y/Y' or 'n/N'\n") 
              
# Function for printout Table with Drives, Caption and check if Removable disk is detected or not
def check_connection_USB() -> str:
    for drive in str(OUTPUT_GET_DRIVE).strip().split("\\r\\r\\n"):
        if "2" in drive:
            drive_caption = drive.split()[0]
            drive_type = drive.split(":")[1].strip()
            if drive_type == "2":
                print(drive_caption + " - Removable disk \n")
                break
    else:  
        if "2" not in drive:
            print("No Removable disk is not connected. Please check connection of USB and try it again!\n")
            
            
# Function for assigned importent Caption
def assigned_table() -> str: 
    print("\nOnly connected drivers: ")
    for item in str(OUTPUT_GET_DRIVE).strip().split("\\r\\r\\n"):
        # Remove ALL spaces in a string, even between words --> described in Library "re" more detailed!
        item = re.sub(r"\s+", " ", item, flags=re.UNICODE)
        if "2" not in item:
            for number in item:
                if number == "0":
                    print(item + " - Unknown")
                elif number == "1":
                    print(item + " - No root directory")    
                elif number == "3":
                    print (item + " - Local disk")
                elif number == "4":
                    print(item + " - Network driver")
    else:
        if number != item:
            print("Not importent for us. If so, please check the table for more information!")
    #countdown_timer()
    
# Separate function for countdown close of process         
def countdown_timer(seconds=3) -> str:
    time.sleep(3)
    while seconds > 0:
        print(f"Process will be terminated in {seconds}...", end="\n")
        time.sleep(1)
        seconds -= 1
    print("\nTerminated...")

# Function for if you want terminated program with other button + magic word help, HELP, Help ==> jiny zapis je neprijatelny!!! -> po zvoleni help se zobrazi prikazy s napovedou co kdo dělá
class Buttons:
    def __init__(self, terminate, back) -> None:
        self.terminate = terminate
        self.back = back
        
    def terminate_button(self): 
        # keyboard.wait('esc')
        print("Wanna terminated process? Press button...")
        while True:
            terminat: str = input(str())
            if not terminat:
    
                print("Wanna terminated process? Press button...")
    print("Are you lost? Please, type secreat command 'Help'...")
    

def main() -> None:
    table()
    check_connection_USB()
    input_for_table()
    assigned_table()
    countdown_timer()
    
    
if __name__ == "__main__":
    main()