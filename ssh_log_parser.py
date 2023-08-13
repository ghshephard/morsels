""" gzipped ssh log parser """
import gzip
from dataclasses import dataclass
from collections import defaultdict
from datetime import datetime
import re
from ipaddress import IPv4Address


RE_FOR_USER=re.compile(r"^.*for (?:[a-z]* )?user (.*?) (?:from|by)")
RE_DATE_STR=re.compile(r"^([^ ]+ [^ ]+ [^ ]+) ")
RE_PID=re.compile(r"^.*sshd\[([0-9]+)]:")
RE_IP=re.compile(r"^.*from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) port")

@dataclass
class Session:
    """ represent ssh sessions"""
    pid: int
    user: str
    opened: datetime
    closed: datetime = None
    ip: IPv4Address = datetime.now()

def get_sessions(filename, year=2017):
    """ Pull out user sessions """
    ip_closed_dt_dic = get_closed_date_ip(filename, year)
    with gzip.open(filename,'rt') as infile:
        for line in infile:
            if "opened for user" in line:
                dt_open=_getdt(line, year)
                name=_getuser(line)
                pid=_getpid(line)
                ip_addr=ip_closed_dt_dic[pid]['ip']
                try:
                    closed_dt=ip_closed_dt_dic[pid]['closed_date']
                except KeyError:
                    closed_dt=None
                yield Session(int(pid), name, dt_open, closed_dt, ip_addr)

def _getip(line):
    if (mtch:= RE_IP.search(line)):
        return mtch.group(1)
    else:
        raise ValueError("No IP found")

def _getuser(line):
    if (mtch := RE_FOR_USER.search(line)):
        return mtch.group(1)
    else:
        raise ValueError("No user found")

def _getdt(line, year):
    if (mtch := RE_DATE_STR.search(line)):
        dstr=mtch.group(1)
        return datetime.strptime( str(year) + dstr, "%Y%b %d %H:%M:%S")
    else:
        raise ValueError("No datetime string found")

def _getpid(line):
    if (mtch := re.search(r"^.*sshd\[([0-9]+)]", line)):
        return mtch.groups()[0]
    else:
        raise ValueError("No PID Found")

def get_closed_date_ip(filename, year):
    """ Pull out ip address and closed date for all PIDs. """
    ip_closed=defaultdict(dict)
    with gzip.open(filename,'rt') as infile:
        for line in infile:
            if "session closed for user" in line:
                pid=_getpid(line)
                date=_getdt(line, year)
                ip_closed[pid]['closed_date']=date
            if any(x in line for x in ["Accepted password for", "Accepted publickey for"]):
                pid=_getpid(line)
                ip_addr=_getip(line)
                ip_closed[pid]['ip']=IPv4Address(ip_addr)


    return ip_closed

def get_user_logins(filename):
    """ Pull out user logins"""
    names=set()
    with gzip.open(filename,'rt') as infile:
        for line in infile:
            if "session opened for user" in line:
                name = _getuser(line)
                if not name in names:
                    names.add(name)
                    yield name

def get_failed_logins(filename):
    """ Pull out Failed logins"""
    failedip=defaultdict(list)
    with gzip.open(filename,'rt') as infile:
        for line in infile:
            if "Failed password" in line:
                name=_getuser(line)
                ip_addr=line.split()[12]
                failedip[ip_addr].append(name)
    return failedip

def main():
    print(Session(1234,"gordon",datetime.now()))
    """ main """
    for user in get_user_logins("sshd.log.gz"):
        print(user)
    print(get_failed_logins("sshd.log.gz"))
    for session in get_sessions("sshd.log.gz", year=2017):
        print(session)
if __name__ == "__main__":
    main()
