import pyshorteners
import time
import os

s = pyshorteners.Shortener()

def Banner():
    print("""  
    
    \033[1;91m      ▒█▀▀█ █░░█ ▀▀█▀▀ ▒█▀▀▄ █▀▀█ █░░░█ █▀▀▄\033[1;m 
    \033[1;91m      ▒█░░░ █░░█ ░░█░░ ▒█░▒█ █░░█ █▄█▄█ █░░█\033[1;m 
    \033[1;32m      ▒█▄▄█ ░▀▀▀ ░░▀░░ ▒█▄▄▀ ▀▀▀▀ ░▀░▀░ ▀░░▀\033[1;m
                        \033[;1mBy D4rk ツ\033[;m 
                                                Version 1.0.1
    """)

def Option():
    print("\n\033[1;32m--- OPTIONS:\033[;m\n")
    print("\033[;1m\033[1;91m + [1]->\033[;m\033[;1m Clck.ru\033[;m\033[;m")
    print("\033[;1m\033[1;91m + [2]->\033[;m\033[;1m Da.gd\033[;m\033[;m")
    print("\033[;1m\033[1;91m + [3]->\033[;m\033[;1m Is.gd\033[;m\033[;m")
    print("\033[;1m\033[1;91m + [4]->\033[;m\033[;1m Os.db\033[;m\033[;m")
    print("\033[;1m\033[1;91m + [5]->\033[;m\033[;1m Qps.ru\033[;m\033[;m")
    print("\033[;1m\033[1;91m + [6]->\033[;m\033[;1m TinyURL.com\033[;m\033[;m")


def Select(opt, url):
    cutdown = pyshorteners.Shortener()
    if(opt == 1):
        try:
            cut = cutdown.clckru.short(url)
            return cut
        except:
            print("\n\033[1;91m* Error -> Try selecting another shortener")
    elif(opt == 2):
        try:
            cut = cutdown.dagd.short(url)
            return cut
        except:
            print("\n\033[1;91m* Error -> Try selecting another shortener")
    elif(opt == 3):
        try:
            cut = cutdown.isgd.short(url)
            return cut
        except:
            print("\n\033[1;91m* Error -> Try selecting another shortener")
    elif(opt == 4):
        try:
            cut = cutdown.osdb.short(url)
            return cut
        except:
            print("\n\033[1;91m* Error -> Try selecting another shortener")
    elif(opt == 5):
        try:
            cut = cutdown.qpsru.short(url)
            return cut
        except:
            print("\n\033[1;91m* Error -> Try selecting another shortener")
    elif(opt == 6):
        try:
            cut = cutdown.tinyurl.short(url)
            return cut
        except:
            print("\n\033[1;91m* Error -> Try selecting another shortener")



def main():
    while True:
        os.system('clear')
        Banner()
        time.sleep(1)
        Option()
        while True:
            val = int(input("\n\033[1;32m--- What is your option -> : \033[;m"))
            
            if(val > 6 or val < 1):
                print("\n\033[1;91m Invalid option !!!\033[;m")
                time.sleep(2)
            else:
                break

        time.sleep(1)
        while True:
            dns = str(input("\n\033[1;32m--- Enter Your URL: \033[;m"))
            if 'http' not in dns:
                print("\n\033[1;91m Invalid URL !!!\033[;m")
                time.sleep(2)
            else:
                break
        
        try:
            Select(val, dns)
            break
        except:
            pass
    time.sleep(1)
    print("\n\033[1;32m--- Your URL:\033[;m \033[;1m" + Select(val, dns))
    time.sleep(1)
    print("\n\033[1;91mEnd :)\n\033[;m")
    time.sleep(1)
#http://www.google.com

if __name__ == '__main__':
	main()