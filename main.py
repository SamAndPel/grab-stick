# GRABSTICK - A python utility to get as much system information as possible in
# as little time as possible. Designed to be run using a USB/rubberducky in an
# ethical hacking environment, but use as you like.

import xml.etree.ElementTree as et
import os
import datetime

from grabstick import grabNetworkConnections


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
        # Do output


def main():
    # Run main() of each getter library (in ./grabstick)
    networks = grabNetworkConnections.main()
    # Concatenate results

    master = networks

    # Render as XML, HTML, TXT for future usage
    writeout(master)


if __name__ == "__main__":
    main()
