import requests
import pyfiglet
out = pyfiglet.figlet_format("SubM3nu", font="slant")
print(out)
domain = input("Enter Domain ==> ")
try:
    worlist= input ("Enter Wordlist Path ==>")
    file = open(f"{worlist}","r")
    content=file.read()
    subdomains=content.splitlines()
    for subdomain in subdomains:
        url1=f"https://{subdomain}.{domain}"
        url2=f"http://{subdomain}.{domain}"
        try:
            requests.get(url1)
            print(f"[+]{url1}")
            requests.get(url2)
            print(f"[+]{url2}")
        except requests.ConnectionError:
            pass
except:
    print("Wordlist not found")
