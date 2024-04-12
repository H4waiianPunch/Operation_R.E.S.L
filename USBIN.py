import os
import wmi

# Currently this waits for USB insertion, then checks whichever drive letter it is for a "private.pem" file
# and it will then display the file in this case.

def detect_usb():
    c = wmi.WMI()
    watcher = c.Win32_VolumeChangeEvent.watch_for("Creation")

    print("Waiting for USB insertion...")

    try:
        while True:
            usb = watcher()
            drive_letter = usb.DriveName.rstrip("\\")

            # Ignore specific drive letters
            if drive_letter != "D:":
                continue

            print(f"USB Drive {drive_letter} has been inserted.")
            break

            # Check if private.pem exists on the USB drive
            #pem_file_path = os.path.join(drive_letter, 'private.pem')
            #print(f"Checking for private.pem at path: {pem_file_path}")
            #if os.path.exists(pem_file_path):
            #    with open(pem_file_path, 'r') as file:
            #        print("Contents of private.pem:")
            #        print(file.read())
            #else:
            #    print("private.pem not found on the USB drive.")

    except KeyboardInterrupt:
        print("Program terminated by user.")

#if __name__ == "__main__":
#   detect_usb()
