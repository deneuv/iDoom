import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Função para verificar se o conteúdo da resposta se parece com um arquivo PDF
def is_pdf(response):
    # Verifica se o conteúdo da resposta parece ser um PDF
    return response.headers.get('content-type') == 'application/pdf'

print("\n")
print(" ... . .. ... . .. ... .. .. ... . .. . . .... ... ... ... ... .. . . .. .. .. .\n\n")
print(" ██╗██████╗  ██████╗  ██████╗ ███╗   ███╗")
print(" ██║██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║  Creator | Deneuv")
print(" ██║██║  ██║██║   ██║██║   ██║██╔████╔██║  Version | iDooM v beta")
print(" ██║██║  ██║██║   ██║██║   ██║██║╚██╔╝██║  Github  | https://github.com/deneuv/iDoom")
print(" ██║██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║  Help    | readme.txt")
print(" ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝")
print("\n ... . .. ... . .. ... .. .. ... . .. . . .... ... ... ... ... .. . . .. .. .. .\n")
proton_mail = "deneuv888399281a1871920312@proton.me"
info_message = "( This is the beta version of iDOOM If you get any \nBug, contact us on {proton_mail} )"
print(" . ... .... ... .. .. ..  m a d e   i n    c y b 3 r i a .. .. . . .... . .... ..\n")
print(f"[Info] {info_message}")

print(" ")
target = str(input("[~] Target URL:"))
param = str(input("[~] Parameter:"))
print("query saved.")
try:
    interval1 = int(input("[~] Interval between:"))
    interval2 = int(input("[~] And:"))
except Exception:
    print("please, use a int number")
    exit()
now = datetime.now()
time1 = now.strftime("%H:%M:%S")
print(f"[ running IDoom | https://github.com/deneuv/iDoom | at {time1} ]")
print("""
 __________________________________________________________________________________________
|                                        RESULTS                                           |
|__________________________________________________________________________________________|
""")

try:
    for line in range(interval1, interval2):
        url = f'{target}{param}{line}'
        response = requests.get(url)
        sizing = len(response.content)
        if response.status_code == 200:
            if is_pdf(response) and sizing > 5000:
                print(url, ' PDF found')
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                if soup.body is not None:
                    body_content = soup.body.get_text()
                    if len(body_content) > 1000:
                        print(url, ' +++++')
                    else:
                        print(url, ' -----')
        else:
            print("error")
except Exception:
    print("something wrong...")
    print("try again.")
    
now = datetime.now()
time2 = now.strftime("%H:%M:%S")
print(f"\n[ finish IDoom | https://github.com/deneuv/iDoom | at {time2} ]")
