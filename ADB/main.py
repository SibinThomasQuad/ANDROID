import subprocess

def run_adb_command(command):
    adb_command = f"adb {command}"
    subprocess.run(adb_command, shell=True)

def prompt_menu():
    print("Select an option:")
    print("1. Get device serial number")
    print("2. Install an APK file")
    print("3. Take a screenshot")
    print("4. Swipe on the screen")
    print("5. Reboot the device")
    print("6. Uninstall an app")
    print("7. List installed packages")
    print("8. Factory Reset (Wipe Data)")
    print("9. Change Device Password")
    print("10. List connected devices")
    print("0. Exit")

while True:
    prompt_menu()
    choice = input("Enter your choice (0-10): ")

    if choice == '0':
        break
    elif choice == '1':
        run_adb_command("devices")
    elif choice == '2':
        apk_path = input("Enter the APK file path: ")
        run_adb_command(f"install {apk_path}")
    elif choice == '3':
        screenshot_path = input("Enter the screenshot file path: ")
        run_adb_command(f"shell screencap -p /sdcard/screenshot.png")
        run_adb_command(f"pull /sdcard/screenshot.png {screenshot_path}")
    elif choice == '4':
        x1, y1, x2, y2, duration = input("Enter swipe coordinates (x1 y1 x2 y2 duration): ").split()
        run_adb_command(f"shell input swipe {x1} {y1} {x2} {y2} {duration}")
    elif choice == '5':
        run_adb_command("reboot")
    elif choice == '6':
        package_name = input("Enter the package name: ")
        run_adb_command(f"uninstall {package_name}")
    elif choice == '7':
        run_adb_command("shell pm list packages")
    elif choice == '8':
        confirmation = input("This action will wipe all data on the device. Are you sure? (Y/N): ")
        if confirmation.upper() == 'Y':
            run_adb_command("shell reboot recovery")
            print("Factory reset initiated. Please follow the on-screen instructions.")
        else:
            print("Factory reset canceled.")
    elif choice == '9':
        old_password = input("Enter the current device password: ")
        new_password = input("Enter the new device password: ")
        run_adb_command(f"shell input keyevent 82")
        run_adb_command(f"shell input text {old_password}")
        run_adb_command(f"shell input keyevent 66")
        run_adb_command(f"shell input text {new_password}")
        run_adb_command(f"shell input keyevent 66")
        print("Device password changed successfully.")
    elif choice == '10':
        run_adb_command("devices")
    else:
        print("Invalid choice. Please try again.\n")
