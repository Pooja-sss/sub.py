import requests
import sys
import pyfiglet
ascii_banner = pyfiglet.figlet_format("SUBDOM ENUM TOOL")
print(ascii_banner)

sub_list = open("wordlist.txt").read()
subs = sub_list.splitlines()

for sub in subs:
    sub_domain = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domain)
    except requests.ConnectionError:
        pass
    else:
        print("Valid domain:", sub_domain)
