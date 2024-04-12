import os
import wmi

# Currently this waits for USB insertion, then checks whichever drive letter it is for a "private.pem" file
# and it will then display the file in this case.

def detect_usb():
    c = wmi.WMI()
    drives = [drive.Caption for drive in c.Win32_LogicalDisk()]
    if "D:" in drives:
        print("USB Drive D: is already inserted.")
        return True
    else:
        print("Waiting for USB insertion...")
        watcher = c.Win32_VolumeChangeEvent.watch_for("Creation")
        try:
            while True:
                usb = watcher()
                drive_letter = usb.DriveName.rstrip("\\")
                if drive_letter == "D:":
                    print(f"USB Drive {drive_letter} has been inserted.")
                    return True
        except KeyboardInterrupt:
            print("Program terminated by user.")
            return False


#def detect_usb():
#    c = wmi.WMI()
#    drives = [drive.Caption for drive in c.Win32_LogicalDisk(DriveType=2)]
#    if drives:
#        print("USB Drive(s) detected:", ", ".join(drives))
#        user_choice = input("Enter the drive letter you want to use (e.g., D, E, F): ").upper() + ":"
#        if user_choice in drives:
#            print(f"Selected USB Drive: {user_choice}")
#            return user_choice
#        else:
#            print("Invalid drive letter. Please select from the available options.")
#            return detect_usb()  # Prompt the user again for input
#    else:
#        print("Waiting for USB insertion...")
#        watcher = c.Win32_VolumeChangeEvent.watch_for("Creation")
#        try:
#            while True:
#                usb = watcher()
#                drive_letter = usb.DriveName.rstrip("\\")
#                print(f"USB Drive {drive_letter} has been inserted.")
#                return drive_letter
#        except KeyboardInterrupt:
#            print("Program terminated by user.")
#            return None