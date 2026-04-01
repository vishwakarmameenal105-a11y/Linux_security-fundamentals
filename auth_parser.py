#!/usr/bin/env python3
"""
Parse Linux auth.log to find failed login attempts
"""

import re
import sys
from collections import Counter

def parse_auth_log(logfile):
    failed_attempts = []
    with open(logfile, 'r') as f:
        for line in f:
            if 'Failed password' in line:
                match = re.search(r'from (\S+)', line)
                if match:
                    failed_attempts.append(match.group(1))
    return failed_attempts

def analyze_failures(failures):
    total = len(failures)
    unique_ips = set(failures)
    top_ips = Counter(failures).most_common(5)
    return total, unique_ips, top_ips

if __name__ == "__main__":
    logfile = sys.argv[1] if len(sys.argv) > 1 else "/var/log/auth.log"
    failures = parse_auth_log(logfile)
    total, unique, top = analyze_failures(failures)
    
    print(f"Total failed attempts: {total}")
    print(f"Unique IPs: {len(unique)}")
    print("Top 5 IPs:")
    for ip, count in top:
        print(f"  {ip}: {count} attempts")
