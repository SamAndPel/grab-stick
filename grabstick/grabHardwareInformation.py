import platform
import socket
import re
import uuid
import json
# import psutil
import logging

# Psutil is not a standard library module so trying to avoid using it for now

# https://stackoverflow.com/a/58420504


def getSystemInfo():
    try:
        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        # info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    print(getSystemInfo())
