import platform

def check_os_version():
    os_name = platform.system()  # Gets the OS name (e.g., Windows, Linux, Darwin for macOS)
    os_version = platform.release()  # Gets the OS version

    return f"Operating System: {os_name} {os_version} - Checked by ZERO-DAY"

# Example usage:
if __name__ == "__main__":
    print(check_os_version())
