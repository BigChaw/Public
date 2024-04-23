import subprocess

# Function for printout Table with Drives, Caption and check if Removable disk is detected or not
def check_connection_USB():
    global output
    output = subprocess.check_output("wmic logicaldisk get drivetype, caption \n", shell=True)
    for drive in str(output).strip().split("\\r\\r\\n"):
        if "2" in drive:
            drive_caption = drive.split()[0]
            drive_type = drive.split(":")[1].strip()
            if drive_type == "2":
                print(drive_caption + " - Removable disk")
    else:
        if "2" not in str(output):
            print("\nNo Removable disk is not connected. Please check connection of USB and try it again!")

if __name__ == "__main__":
    check_connection_USB()  