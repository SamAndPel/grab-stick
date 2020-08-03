import subprocess


def get_networks():
    # Return array of saves network SSIDs on the local machine
    # List network names in CMD
    output = str(subprocess.check_output("netsh wlan show profile"))
    # Parse output from CMD
    section = output[output.find("User profiles") + 13::].split("\\r\\n")
    networknames = []
    for potential in section:
        if "Profile" in potential:
            networknames.append(potential.split(":")[1].strip())
    return networknames


def get_details(ssid):
    # Get network details from SSID
    output = str(subprocess.check_output(
        f'netsh wlan show profile "{ssid}" key=clear'))
    # Parse output from CMD
    details = output.split("\\r\\n")
    print(ssid)
    print(*details, sep='\n')


if __name__ == "__main__":
    get_networks()
