# grab-stick
Stored at: [https://github.com/SamAndPel/grab-stick](https://github.com/SamAndPel/grab-stick)
A set of python utilities to rapidly gather system data.

Designed for Windows 10, but may extend to Linux in the future.

## Installation/usage
1. Run pip install to install all required modules from requirements.txt
2. Run main.py

## Design
./grabstick contains a series of python libraries, each which extracts one element of system data, returning a DICT.
Main.py runs each of these, and renders the output to JSON in a folder named for the time and date of the scan.

The system can be extended by creating more scripts in ./grabstick, and importing them into main.py

Originally designed to autorun on USB insert (hence the name 'grabstick'), this feature had to be cut due to lack of
time and unexpected complexity. I may implement it in the future.

## Features
- [x] Grab basic hardware information
- [x] Grab local OS version
- [x] Grab local user account names
- [x] Grab local groups, and the users in every group
- [x] Grab local network connection history, names and passwords
- [x] Grab all running processes, and relevant info about each
- [ ] Grab any accessible SSH keys
- [ ] Uses threading to optimise speed
- [x] Export to JSON for easy visualisation at a later date

## Stretch features
- [ ] Script autoruns on USB plugin
- [ ] Store all collected data on the USB stick, then automatically eject itself
- [ ] Grab encrypted password hashes from SAM/shadow file
- [ ] Emulate a USB keyboard/network device (may have to move to another platform - Raspberry Pi Zero?)
- [ ] Disguise running scripts as system processes
- [ ] Similar functionality on Linux devices
- [ ] Escalate privileges to get extra data
- [ ] Purge relevant logs before disconnect (may require root)
