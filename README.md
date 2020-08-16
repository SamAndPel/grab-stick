# grab-stick
A set of python utilities to automatically exfiltrate system data on USB insert.

Designed for Windows 10, but may extend to linux in the future.

## Design
./grabstick contains a series of python libraries, each which extracts one element of system data, returning a DICT.
Main.py runs each of these in parallel using threading for optimal speed, and renders the output to XML and TXT in a
folder named for the ttime and date of the scan.

The system can be extended by creating more scripts in ./grabstick, and importing them into main.py

## Features
- [ ] Script autoruns on USB plugin
- [ ] Grab local OS/critical software versions
- [ ] Grab local user account names and encrypted password hashes
- [ ] Grab local network connection history, names and passwords
- [ ] Grab any accessible SSH keys
- [ ] Uses threading to optimise speed
- [ ] Store all collected data on the USB stick, then automatically eject itself

## Stretch features
- [ ] Emulate a USB keyboard/network device (may have to move to another platform - Raspbery Pi Zero?)
- [ ] Disguse running scripts as system processes
- [ ] Similar functionality on Linux devices
- [ ] Escalate privileges to get extra data
- [ ] Purge relevant logs before disconnect (may require root)