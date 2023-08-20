import subprocess

blocked_ips = set()

def block_ip(ip):
    if ip in blocked_ips:
        print(f"Ip {ip} is already blocked. ")

    iptables = f"iptables -I INPUT -s {ip} -j DROP"
    subprocess.run(iptables, shell=True)
    blocked_ips.add(ip)
    print(f"Blocked IP: {ip}")
fails = {}

def check(ip):
    if ip in fails:
        fails[ip] += 1
    else:
        fails[ip] = 1

    if fails[ip] >= 3:
        block(ip)

def block(ip):
    print(f"Blocking ip {ip}")


LOG_FILE = "/var/log/auth.log"


with open(LOG_FILE, "r") as log_file:
    for i in log_file:
        if "Failed password" in i:
            ip = i.split()[-4]
            print(f"Gtel enq es ipov block {ip}")
            check(ip.strip())
