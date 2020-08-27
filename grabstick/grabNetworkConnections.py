import subprocess


def get_networks():
    # Return array of saved network SSIDs on the local machine
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
    # Return dict of details
    output = str(subprocess.check_output(
        f'netsh wlan show profile "{ssid}" key=clear'))
    # Parse output from CMD
    lines = output.split("\\r\\n")
    details = {}
    for i, line in enumerate(lines):
        if ":" in line and i != 1:
            key = line[:line.find(":"):].strip()
            value = line[line.find(":") + 1::].strip()
            details[key] = value
    return details


def main():
    networks = get_networks()
    details = {}
    for ssid in networks:
        details[ssid] = get_details(ssid)
    return details
