# grab-stick
A set of python utilities to automatically exfiltrate system data on USB insert
Designed for Windows 10, but may extend to linux in the future

## Features
- [ ] Script autoruns on USB plugin
- [ ] Grab local OS/critical software versions
- [ ] Grab local user account names and encrypted password hashes
- [ ] Grab local network connection history, names and passwords
- [ ] Grab any accessible SSH keys
- [ ] Store all collected data on the USB stick, then automatically eject itself

## Stretch features
- [ ] Emulate a USB keyboard/network device (may have to move to another platform - Raspbery Pi Zero?)
- [ ] Disguse running scripts as system processes
- [ ] Similar functionality on Linux devices
- [ ] Escalate privileges to get extra data
- [ ] Purge relevant logs before disconnect (may require root)