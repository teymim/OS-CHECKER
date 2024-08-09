import platform
import socket

def check_os_version(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        os_name = platform.system()
        os_version = platform.release()

        return f"Operating System on {hostname} ({ip_address}): {os_name} {os_version} - Checked by ZERO-DAY"
    except Exception as e:
        return f"Unable to retrieve OS information for {ip_address}: {str(e)}"

if __name__ == "__main__":
    ip_to_check = input("Enter the IP address you want to check: ")
    print(check_os_version(ip_to_check))
