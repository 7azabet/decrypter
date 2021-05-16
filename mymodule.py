# Colors
# Bold
############
black = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
y = "\033[1;33m"  # Yellow
b = "\033[1;32m"  # Blue
sec = 's'
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
############

import os
import socket
import time


def system(command):
    os.system(command)


try:
    from tqdm import tqdm
except Exception as e:
    system('pip3 install tqdm; python3 decrypt.py')


def clear():
    os.system("clear")


def wait():
    print('Wait..')
    time.sleep(0.2)


def space():
    print('')


nc = 'n'


def banner():
    clear()
    print('\033[1;37m')
    print(f"""
    
                {b}All th@nks t0 All@h ({y}My God{b}){W}

    ███████╗██╗         ██╗  ██╗ ██████╗ ██████╗ ███████╗ █████╗ ███╗   ██╗
    ██╔════╝██║         ██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗████╗  ██║
    █████╗  ██║         █████╔╝ ██║   ██║██████╔╝███████╗███████║██╔██╗ ██║
    ██╔══╝  ██║         ██╔═██╗ ██║   ██║██╔══██╗╚════██║██╔══██║██║╚██╗██║
    ███████╗███████╗    ██║  ██╗╚██████╔╝██║  ██║███████║██║  ██║██║ ╚████║
    ╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                
                    {W}Was Coded By - [{R}7AZABET{W}] - {G}@curlwget {W}                                                                      
    """)


eic = 'a'


def test_connection():
    try:
        print(W + 'Checking Your Internet Connection...')
        time.sleep(2)
        socket.create_connection(("information-eg.blogspot.com", 80))
        print('\033[1;32m[+] You Are Connected')
        time.sleep(1)
        clear()
    except (OSError, socket.gaierror):
        print(R + '[!] You Are N0T Connected To The Internet')
        exit()
