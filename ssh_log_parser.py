""" gzipped ssh log parser """
import gzip
from dataclasses import dataclass
from collections import defaultdict
from datetime import datetime
import re



def get_user_logins(filename):
    """ Pull out user logins"""
    names=set()
    with gzip.open(filename,'rt') as infile:
        for line in infile:
            if "session opened for user" in line:
                name=line.split()[10]
                if not name in names:
                    names.add(name)
                    yield name

def get_failed_logins(filename):
    """ Pull out Failed logins"""
    failedip=defaultdict(list)
    with gzip.open(filename,'rt') as infile:
        for line in infile:
            if "Failed password" in line:
                name=line.split()[10]
                ip_addr=line.split()[12]
                failedip[ip_addr].append(name)
    return failedip

def main():
    """ main """
    for user in get_user_logins("sshd.log.gz"):
        print(user)
    print(get_failed_logins("sshd.log.gz"))
    for session in get_user_sessions("sshd.log.gz"):
        print(session)
if __name__ == "__main__":
    main()
