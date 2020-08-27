import os
import psutil
import time
from datetime import datetime

def get_running_processes():
    # Iterate over all running process
    processes = []
    for proc in psutil.process_iter():
        try:
            procinfo = {}
            # Get process info
            procinfo["name"] = proc.name()
            procinfo["pid"] = proc.pid
            # procinfo["cpu"] = proc.cpu_percent(interval=None)
            # Commentedout as this requires an interval to time over, setting interval >1ms creates enormous slowdown
            procinfo["ram"] = str(round((proc.memory_full_info().uss / (1024.0 ** 2)), 3)) + "mb"
            procinfo["user"] = proc.username()
            procinfo["status"] = proc.status()
            procinfo["priority"] = int(proc.nice())
            procinfo["threads_spawned"] = proc.num_threads()

            processes.append(procinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def main():
    return get_running_processes()
