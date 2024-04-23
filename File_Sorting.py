import sys
import os
import subprocess
import time

USER = os.getlogin()
NOTEPAD = "C:\\Windows\\System32\\notepad.exe"
BASE_PATH = f"c:\\Users\\{USER}\\Desktop\\"
DRIVERS = f"{BASE_PATH}Drivers.txt"
ENCODED = f"{BASE_PATH}Encoded.txt"
FINAL_CUT = "Final_cut.txt"
FINAL = f"{BASE_PATH}{FINAL_CUT}"
NO_BLANKS = f"{BASE_PATH}No_blanks.txt"
COUNT_LINES = f"{BASE_PATH}Count_lines.txt"
        
def list_drivers():
    subprocess.Popen("driverquery -fo csv > C:\\Users\\Mfryj\\Desktop\\Drivers.txt", shell= True)

    time.sleep(2)

def delete_quetes_comma():
    file = open(f"{DRIVERS}", "r")
    file = file.read().replace('"', '').replace(',', '|') 
    
    sys.stdout = open(f"{ENCODED}", "w", encoding="UTF-8") # Works only for English version of Win!!!
    sys.stdout.write(f"{file}")
    
def add_numbers_lines():
    c = open(f"{NO_BLANKS}", "r")
    list_of_lines = c.readlines()
    c.close()
    
    # Addiding numbers
    number = 0 # --> je to nadpisek v souborech!!!!!!!!!!!!!!!!!!
    numbered_list_of_lines = []
    for i in list_of_lines:
        numbered_lines = "{0:0>1}".format(number) + "." + i
        numbered_list_of_lines.append(numbered_lines)
        number += 1
    f = open(f"{FINAL}", "w")
    for i in numbered_list_of_lines:
        f.write(i)
    f.close()         

# Function for delete blank lines 
def delete_blank():
    lines = []
    with open(f"{ENCODED}", "r") as f:
        for line in f:
            if len(line) > 1:
                lines.append(line)
    with open(f"{NO_BLANKS}", "w") as f:
        for number, line in enumerate(lines):
            if not number % 2 != 0:
                f.write(line)
                print(line)
                
# Function for counting of lines in files 
def count_lines():
    with open(f"{FINAL}", "r") as fp:
        for count, line in enumerate(fp):

            with open(f"{COUNT_LINES}", "w") as cnt:
                cnt.writelines(str('Number of lines: ' f"{count}" + " - " + f"{FINAL_CUT}"))
                
# Function for deleting last line in file 
def delete_last_line():
    fd = open (f"{FINAL}", "r")
    d = fd.read()
    fd.close()
    last_line = d.split("\n")
    s = "\n".join(last_line[:-1])
    fd = fd = open (f"{FINAL}", "w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()

# Function for closing opend files                
def open_close_files():
    out = subprocess.Popen([NOTEPAD, FINAL])
    time.sleep(3)
    out.terminate() 
    
    cnt_ln = subprocess.Popen([NOTEPAD, COUNT_LINES])
    time.sleep(3)
    cnt_ln.terminate()
    
# Remove file/files
def delete_files():
   if (
       os.path.isfile(DRIVERS)
       and os.path.isfile(NO_BLANKS)
    ):
        os.remove(DRIVERS)
        os.remove(NO_BLANKS)

if __name__ == "__main__":
    list_drivers()
    delete_quetes_comma()
    delete_blank()
    add_numbers_lines()
    delete_last_line()
    count_lines()
    open_close_files()
    delete_files()
