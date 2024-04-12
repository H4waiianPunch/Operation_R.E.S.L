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