import requests
from bs4 import BeautifulSoup
from datetime import datetime
from termcolor import colored

# Função para verificar se o conteúdo da resposta se parece com um arquivo PDF
def is_pdf(response):
    # Verifica se o conteúdo da resposta parece ser um PDF
    return response.headers.get('content-type') == 'application/pdf'

print("\n")
print(colored(" ... . .. ... . .. ... .. .. ... . .. . . .... ... ... ... ... .. . . .. .. .. .\n\n", "blue"))
print(colored(" ██╗██████╗  ██████╗  ██████╗ ███╗   ███╗", "green") + colored("", "red"))
print(colored(" ██║██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║", "green") + colored("  Creator | ", "white") + colored("Deneuv", "red"))
print(colored(" ██║██║  ██║██║   ██║██║   ██║██╔████╔██║", "cyan") + colored("  Version | ", "white") + colored("iDooM v beta", "green"))
print(colored(" ██║██║  ██║██║   ██║██║   ██║██║╚██╔╝██║", "cyan") + colored("  Github  | ", "white") + colored("https://github.com/deneuv/iDoom", "green"))
print(colored(" ██║██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║", "blue") + colored("  Help    | ", "white") + colored("readme.txt", "yellow"))
print(colored(" ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝", "blue") + colored("", "red"))
print(colored("\n ... . .. ... . .. ... .. .. ... . .. . . .... ... ... ... ... .. . . .. .. .. .\n", "blue"))
proton_mail = "deneuv888399281a1871920312@proton.me"
info_message = f"( This is the beta version of iDOOM If you get any \nBug, contact us on {proton_mail} )"
print(colored(" . ... .... ... .. .. ..  m a d e   i n    c y b 3 r i a .. .. . . .... . .... ..\n", "magenta"))
print(colored(f"[Info] {info_message}", "yellow"))

print(" ")
target = str(input(colored("[~]", "blue") + colored(" Target URL:", "white")))
param = str(input(colored("[~]", "blue") + colored(" Parameter:", "white")))
print(colored("query saved.", "green"))
try:
    interval1 = int(input(colored("[~]", "blue") + colored(" Interval between:", "white")))
    interval2 = int(input(colored("[~]", "blue") + colored(" And:", "white")))
except Exception:
    print(colored("please, use a int number", "red"))
    exit()
now = datetime.now()
time1 = now.strftime("%H:%M:%S")
print(f"[ running IDoom | https://github.com/deneuv/iDoom | at {time1} ]")
print(colored("""
 __________________________________________________________________________________________
|                                        RESULTS                                           |
|__________________________________________________________________________________________|
""", "blue"))

try:
    for line in range(interval1, interval2):
        url = f'{target}{param}{line}'
        response = requests.get(url)
        sizing = len(response.content)
        if response.status_code == 200:
            if is_pdf(response) and sizing > 5000:
                print(colored(url, 'green'), colored('PDF found', 'green'))
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                if soup.body is not None:
                    body_content = soup.body.get_text()
                    if len(body_content) > 1000:
                        print(colored(url, 'yellow'), colored('+++++', 'yellow'))
                    else:
                        print(colored(url, 'yellow'), colored('-----', 'yellow'))
        else:
            print(colored("error", 'red'))
except Exception:
    print(colored("something wrong...", 'red'))
    print(colored("try again.", 'red'))
    
now = datetime.now()
time2 = now.strftime("%H:%M:%S")
print(f"\n[ finish IDoom | https://github.com/deneuv/iDoom | at {time2} ]")
