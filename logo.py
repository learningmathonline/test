from distutils.core import setup
import os


logo = """
________  ________ __________ _________                    
\_____  \ \_____  \\______   /   _____/                    
 /   |   \ /   |   \|     ___\_____  \                     
/    |    /    |    |    |   /        \                    
\_______  \_______  |____|  /_______  /                    
        \/        .____    .___ _______   ____ _______  ___
A program for     |    |   |   |\      \ |    |   \   \/  /
cyberpatroit      |    |   |   |/   |   \|    |   /\     / 
Ubuntu Systems    |    |___|   /    |    |    |  / /     \ 
#GetLinux         |_______ |___\____|__  |______/ /___/\  \ 
                          \/           \/               \_/
"""
menu = "1: Get All Files\n2: Change User Password\n3: Get All Users\n4: Generate New Passkey\n5: Local Policy's\n6: Quit\n"

polocies = """
1: Check Ports
2: Network
3: Directory Access
4: Excute Permission
"""

def startup():
    print(logo)
    print(menu)
    choiceinput = input("Ente Number Value>>>")
    try:
        choiceinput = int(choiceinput)
    except:
        return
    if choiceinput == 1:
        pass #get all files
    elif choiceinput == 2:
        pass #Change User Password
    elif choiceinput == 3:
        pass #get all users
    elif choiceinput == 4:
        pass #Gen new password
    elif choiceinput == 5:
        print(polocies)
    elif choiceinput == 6:
        pass #quit
    else:
        return

if  __name__ == '__main__':
    startup()