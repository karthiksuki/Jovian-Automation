import os
import platform
import sys
import requests
import urllib3
from colorama import Fore
from txt.header import lb_header
from txt.help import *
from txt.startup import *

print("      __                       ___  __              ___       __   __       ")
print("   | /  \ \  / |  /\  |\ |    |__  |__)  /\   |\/| |__  |  | /  \ |__) |__/ ")
print("\__/ \__/  \/  | /~~\ | \|    |    |  \ /~~\  |  | |___ |/\| \__/ |  \ |  \ ")

print("")

# Check if the system is running Python 3
if sys.version[0] == '2':
    print("[!] Please use Python 3")
    sys.exit()

# Checks whether the pc is connect to internet

urlConnected = "http://www.jovian.ai"
timeout = 5

try:
    request = requests.get(urlConnected, timeout=timeout)
    print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
    print("No Internet Connection, Protip: Connect to Internet and try again")

print("")

# Username validator

Jovian_website = 'https://jovian.ai/'

Jovian_api_url = 'https://jovian.ai/api/user/'

Jovian_profile = input('Enter your jovian Username - ')

profile_url = Jovian_api_url + Jovian_profile

print("")

http = urllib3.PoolManager()
error = http.request("GET", profile_url)
if error.status == 404:
    print("Incorrect Username")


# Clear the Terminal 
def clear():
    if os.name == 'nt':
        return os.system('cls')
    else:
        return os.system('clear')


# Print the menu again

def menu():
    print(lb_header())
    print(menu)


# install jovian
def installJovian():
    if os.name == 'nt':
        return os.system('pip install jovian --upgrade')
    else:
        return os.system('pip3 install jovian --upgrade')


# install jupyterlab
def installjupyterlab():
    if os.name == 'nt':
        return os.system('pip install jupyterlab')
    else:
        return os.system('pip3 install jupyterlab')


# install jupyter notebook
def installjupyternotebook():
    if os.name == 'nt':
        return os.system('pip install notebook')
    else:
        return os.system('pip3 install notebook')


os.system("printf '\033]2;Jovian Framework\a'")

print("")

print("Name of the OS:", platform.system())

print("")

print("Version of the operating system:", platform.release())

print("")

print(Options)

# Colours
warning = "[" + Fore.RED + "!" + Fore.RESET + "]"
question = "[" + Fore.YELLOW + "?" + Fore.RESET + "]"
information = "[" + Fore.BLUE + "Thank you" + Fore.RESET + "]"
wait = "[" + Fore.MAGENTA + "*" + Fore.RESET + "]"
found = "[" + Fore.GREEN + "+" + Fore.RESET + "]"
tired = "[" + Fore.CYAN + "-" + Fore.RESET + "]"

# Input
try:
    while True:
        choix = input("\n Jovian Framework(" + Fore.BLUE + "~" + Fore.RESET + ")$ ")

        if choix.lower() == 'h' or choix.lower() == 'help':
            clear()
            menu()
            print(help)

        elif choix.lower() == 'c' or choix.lower() == 'install':
            clear()
            menu()
            print('Installing the jovian Library on your computer please wait...')

            print(installJovian())

            print("")

            print(Aftercode)

            while True:
                choix = input("\n Jovian Framework(" + Fore.BLUE + "~" + Fore.RESET + ")$ ")

                if choix.lower() == 'b' or choix.lower() == 'back':
                    clear()
                    startup()
                    break
                elif choix.lower() == 'h' or choix.lower() == 'help':
                    clear()
                    menu()
                    print(help)
                elif choix.lower() == 'e' or choix.lower() == 'exit':
                    sys.exit("\n" + information + " Bye ! :)")
                else:
                    print("\033[1;31mSorry, that was an invalid command!\033[1;m")

        elif choix.lower() == 'e' or choix.lower() == 'exit':
            sys.exit("\n" + information + " Bye ! :)")

        elif choix.lower() == 'clear':
            clear()
            startup()
            break

        elif choix == '1':
            clear()
            menu()
            print(Jovian_Notebook)

            while True:
                choix = input("\n Jovian Framework(" + Fore.BLUE + "~" + Fore.RESET + ")$ ")

                if choix.lower() == 'h' or choix.lower() == 'help':
                    clear()
                    menu()
                    print(help)

                elif choix.lower() == 'clear':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'b' or choix.lower() == 'back':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'c' or choix.lower() == 'install':
                    clear()
                    menu()
                    print('Installing the jovian Library on your computer please wait...')

                    installJovian()

                elif choix.lower() == 'e' or choix.lower() == 'exit':
                    sys.exit("\n" + information + " Bye ! :)")

                elif choix.lower() == '1' or choix.lower() == 'jovian clone':
                    urlDownload = input('Jovian Notebook to install (Jovian Profile + Notebook) - ')

                    try:
                        response = requests.get(Jovian_website + urlDownload)
                        print("URL is valid and exists on the Jovian Website")
                    except requests.ConnectionError as exception:
                        print("URL does not exist on Internet")

                    print("")

                    # Download the Notebook
                    def downloadNotebook():
                        if os.name == 'nt':
                            os.system('jovian clone ' + urlDownload)
                            print("")
                            print('Success')
                        else:
                            os.system('jovian clone ' + urlDownload)
                            print("")
                            print('Success')


                    downloadNotebook()

                    print(Aftercode)
                else:
                    print("\033[1;31mSorry, that was an invalid command!\033[1;m")

        elif choix == '2':
            clear()
            menu()
            print(Commit_Repo)

            while True:
                choix = input("\n Jovian Framework(" + Fore.BLUE + "~" + Fore.RESET + ")$ ")

                if choix.lower() == 'h' or choix.lower() == 'help':
                    clear()
                    menu()
                    print(help)

                elif choix.lower() == 'b' or choix.lower() == 'back':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'clear':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'e' or choix.lower() == 'exit':
                    sys.exit("\n" + information + " Bye ! :)")

                elif choix.lower() == 'c' or choix.lower() == 'install':
                    clear()
                    menu()
                    print('Installing the jovian Library on your computer please wait...')

                    installJovian()

                elif choix.lower() == '1' or choix.lower() == 'commit':
                    pathCommit = input('Path = ')

                    # Commit to Jovian
                    def commitJovian():
                        if os.name == 'nt':
                            os.system('jovian commit ' + pathCommit)
                            print("")
                            print('Success')

                        else:
                            os.system('jovian commit ' + pathCommit)
                            print("")
                            print('Success')


                    print(commitJovian())

                    print(Aftercode)
                else:
                    print("\033[1;31mSorry, that was an invalid command!\033[1;m")

        elif choix == '3':
            clear()
            menu()
            print(GitHub_Repo)

            while True:
                choix = input("\n Jovian Framework(" + Fore.BLUE + "~" + Fore.RESET + ")$ ")

                if choix.lower() == 'h' or choix.lower() == 'help':
                    clear()
                    menu()
                    print(help)

                elif choix.lower() == 'b' or choix.lower() == 'back':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'clear':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'c' or choix.lower() == 'install':
                    clear()
                    menu()
                    print('Installing the jovian Library on your computer please wait...')

                    installJovian()

                elif choix.lower() == 'e' or choix.lower() == 'exit':
                    sys.exit("\n" + information + " Bye ! :)")

                elif choix.lower() == '1' or choix.lower() == 'git clone':
                    gitClone = input('GITHUB REPOSITORY URL = ')
                    check_git_folder_exists = os.path.exists("GitHub_Repo")

                    # Git Clone
                    def gitCloner():
                        if os.name == 'nt':
                            check_git_folder_exists or os.system('mkdir GitHub_Repo')
                            os.system('dir GitHub_Repo')
                            os.system('git clone ' + gitClone)
                            print("")
                            print('Success')
                        else:
                            check_git_folder_exists or os.system('mkdir GitHub_Repo')
                            os.system('cd GitHub_Repo')
                            os.system('git clone ' + gitClone)
                            print("")
                            print('Success')


                    gitCloner()

                    print(Aftercode)

                else:
                    print("\033[1;31mSorry, that was an invalid command!\033[1;m")

        elif choix == '4':
            clear()
            menu()
            print(Jupyter_Notebook)

            while True:
                choix = input("\n Jovian Framework(" + Fore.BLUE + "~" + Fore.RESET + ")$ ")

                if choix.lower() == 'h' or choix.lower() == 'help':
                    clear()
                    menu()
                    print(help)

                elif choix.lower() == 'b' or choix.lower() == 'back':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'clear':
                    clear()
                    startup()
                    break

                elif choix.lower() == 'c' or choix.lower() == 'install':
                    clear()
                    menu()
                    print('Installing the jovian Library on your computer please wait...')

                    installJovian()

                elif choix.lower() == 'e' or choix.lower() == 'exit':
                    sys.exit("\n" + information + " Bye ! :)")

                elif choix.lower() == '1' or choix.lower() == 'jupyter open':
                    clear()
                    menu()

                    installjupyterlab()

                    print("")
                    print("")

                    jupyterlabOpen = input('Folder or File Path (Optional): ')

                    os.system('jupyter-lab --allow-root -y ' + jupyterlabOpen)
                    print(Aftercode)

                elif choix.lower() == '2' or choix.lower() == 'jupyter notebook':
                    clear()
                    menu()

                    installjupyternotebook()

                    print("")
                    print("")

                    jupyternotebookOpen = input('Folder or File Path (Optional): ')

                    os.system('jupyter-notebook --allow-root -y ' + jupyternotebookOpen)

                    print(Aftercode)
                else:
                    print("\033[1;31mSorry, that was an invalid command!\033[1;m")

        elif choix == 'e' or choix.lower() == 'exit':
            sys.exit("\n""Bye ! :")

        elif choix == 'help':
            clear()
            menu()
            print(help)

        else:
            print("\033[1;31mSorry, that was an invalid command!\033[1;m")

except KeyboardInterrupt:
    sys.exit("\n""Bye ! :")
