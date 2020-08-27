# GRABSTICK - A python utility to get as much system information as possible in
# as little time as possible. Designed to be run using a USB/rubberducky in an
# ethical hacking environment, but use as you like.

import os
import datetime
import json

from grabstick import grabNetworkConnections, grabHardwareInformation, grabRunningProcesses


def writeout(data):
    """
    data contains a list of dicts, write them to XML, txt and(?) HTML for output
    """
    ts = datetime.datetime.now()
    time = ts.strftime("%H-%M")
    date = ts.strftime("%d-%m-%Y")
    title = f"Scan at {time} on {date}"

    dir = os.path.join(os.getcwd(), title)
    if os.path.exists(dir):
        print("Error - path already exists, exiting")
    else:
        os.mkdir(dir)
        os.chdir(dir)
        # Do output
        with open("Scanresults.json", "w") as file:
            json.dump(data, file)


def main():
    # Run main() of each getter library (in ./grabstick)
    networks = grabNetworkConnections.main()
    hardware = grabHardwareInformation.main()
    processes = grabRunningProcesses.main()

    # Concatenate results
    master = {}
    master["networks"] = networks
    master["hardware"] = hardware
    master["processes"] = processes

    # Render as JSON for future usage
    writeout(master)


if __name__ == "__main__":
    main()
