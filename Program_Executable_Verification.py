import os
import subprocess
import time
import sys

Programs = []
user = os.getlogin()
base_route = f"c:\\Users\\{user}\\Desktop\\"
Programs_32 = f"{base_route}Programs_System32.txt"
Installed_Programs = f"{base_route}Installed_Programs.txt"
Verifiability_executability = f"{base_route}Verifiability_executability.txt"
Notepad_exe = "C:\\Windows\\System32\\notepad.exe"

# Searching through files with suffix ".exe" and export them to .txt file
def suffix_exe():
    for dirpath, dirnames, filenames in os.walk("c:\\Windows\\System32"):
        for filename in filenames:
            if filename.endswith(".exe"):
                Programs.append(filename)
        export = open(Programs_32, "w")
        export.write(f"Content of System32:\n {Programs} \n")
        export.close()
        
# Start/Close of Programs_System32.txt        
def programs_syste32():
    filen = Programs_32
    note = Notepad_exe
    procc = subprocess.Popen([note, filen])
    time.sleep(10)
    procc.terminate()

time.sleep(2)

def programs_write_down():
# Cycle for search selected program and write down to .txt file
    while Programs:
        for Program in Programs:
            if Program != "mspaint.exe":
                continue
            log = open(Installed_Programs, "w")
            log.write(f"1. {Program} - included! \n")
            log.close()
            if "mspaint.exe" not in Program:
                log = open(Installed_Programs, "a")
                log.write("File is not included!")

            for Program in Programs:
                if Program != "calc.exe":
                    continue
                log = open(Installed_Programs, "a")
                log.write(f"2. {Program} - included! \n")

                for Program in Programs:
                    if Program != "SnippingTool.exe":
                        continue
                    log = open(Installed_Programs, "a")
                    log.write(f"3. {Program} - inlcuded! \n")

                    for Program in Programs:
                        if Program != "notepad.exe":
                            continue
                        log = open(Installed_Programs, "a")
                        log.write(f"4. {Program} - included! \n")
                    log.close()
                log.close()
            log.close()
        break
    
# Start/Close of Installed_Programs.txt
def Installed_programs():
    filen = Installed_Programs
    note = Notepad_exe
    procc = subprocess.Popen([note, filen])
    time.sleep(10)
    procc.terminate()

time.sleep(2)

# Function for start and terminated Paint
def msapint():
    subprocess.run(["powershell", "-Command", "mspaint"])
    time.sleep(2)
    task_kill = subprocess.run(
        ["powershell", "-Command", "taskkill /IM mspaint.exe /F"], capture_output=True
    )
    time.sleep(1)
    with open(Verifiability_executability, "w") as sys.stdout:
        print(task_kill)

# Function for start and terminated Calculator
def calc():
    subprocess.run(["powershell", "-Command", "calc"])
    time.sleep(2)
    task_kill = subprocess.run(
        ["powershell", "-Command", "taskkill /IM CalculatorApp.exe /F"],
        capture_output=True,
    )
    time.sleep(1)
    with open(Verifiability_executability, "a") as sys.stdout:
        print(task_kill)

# Function for start and terminated SnippingTool
def SnippingTool():
    subprocess.run(["powershell", "-Command", "SnippingTool"])
    time.sleep(2)
    task_kill = subprocess.run(
        ["powershell", "-Command", "taskkill /IM SnippingTool.exe /F"],
        capture_output=True,
    )
    time.sleep(1)
    with open(Verifiability_executability, "a") as sys.stdout:
        print(task_kill)

# Function for start and terminated NotePad
def NotePad():
    subprocess.run(["powershell", "-Command", "notepad"])
    time.sleep(2)
    task_kill = subprocess.run(
        ["powershell", "-Command", "taskkill /IM notepad.exe /F"], capture_output=True
    )
    time.sleep(1)
    with open(Verifiability_executability, "a") as sys.stdout:
        print(task_kill)

# Start/Close of Overitelnost_spustitelnost.txt
def verification_lunchable():
    filen = Verifiability_executability
    note = Notepad_exe
    procc = subprocess.Popen([note, filen])
    time.sleep(10)
    procc.terminate()

time.sleep(5)

# Function for delete those files at the end of script
def delete_files():
    if (
        os.path.isfile(Installed_Programs)
        and os.path.isfile(Programs_32)
    ):
        os.remove(Installed_Programs)
        os.remove(Programs_32)
        

if __name__ == "__main__":
    suffix_exe()
    programs_syste32()
    programs_write_down()
    Installed_programs()
    msapint()
    calc()
    SnippingTool()
    NotePad()
    verification_lunchable()
    delete_files()