 	## Prerequisites

- **Linux** (Ubuntu, Debian, RHEL, etc.)
- **Python 3** (usually pre-installed on most Linux distros)

### Check if Python is installed

```bash
python3 --version

# Linux_security-fundamentals
Basic scripts for log analysis, system monitoring, and detection — building from the ground up

## Requirements
- Linux (Ubuntu, Debian, RHEL, etc.)
- Python 3
- Access to `/var/log/auth.log` (requires sudo on some systems)

## Usage
```bash
sudo python3 auth_parser.py /var/log/auth.log
