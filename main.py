import ctypes
import string
import os
import discord_webhook
import numpy
import time
LICNECE = """
MIT License

Copyright (c) 2022 DanceOfEternity 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:  # Check if the requrements have been installed
    from discord_webhook import DiscordWebhook  # Try to import discord_webhook
except ImportError:  # If it chould not be installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:  # Setup try statement to catch the error
    import requests  # Try to import requests
except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()  # Exit the program
try:  # Setup try statement to catch the error
    import numpy  # Try to import requests
except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()  # Exit the program

# check if user is connected to internet
url = "https://github.com"
try:
    response = requests.get(url)  # Get the responce from the url
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    # Tell the user
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()  # Exit program


class NitroGenerator:  # Initialise the class
    def __init__(self):  # The initaliseaiton function
        self.fileName = "Nitros.txt"  # Set the file name the codes are stored in

    def main(self):  # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        if os.name == "nt":  # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Made by Drillenissen#4268")  # Change the
        else:  # Or if it is unix
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a',
                  end='', flush=True)  # Update title of command prompt

        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """)  # Print the title card
        time.sleep(2)
        self.slowType("Made by: DanceOfEternity && yigitsalar", .02)
        time.sleep(1)
        self.slowType(
            "\nHow Many Codes to Generate and Check: ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()

        if USE_WEBHOOK:
           
            self.slowType(
                "If you want to use a Discord webhook, type it here or press enter to ignore: ", .02, newLine=False)
            url = input('')
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook( 
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()

        valid = []  
        invalid = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 24])
        for s in c: 
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}" 

                result = self.quickChecker(url, webhook) 

                if result: 
                    
                    valid.append(url)
                else:  
                    invalid += 1  
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break  

            except Exception as e: 
                print(f" Error | {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid ") 
                print("")
            else:  
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid \a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")  

        
        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]  

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
        # Generate the request url
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  

        if response.status_code == 200: 
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitros.txt", "w") as file:  
                file.write(nitro)

            if notify is not None:  # If a webhook has been added
                DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                    url=url,	
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True 

        else:
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGenerator()  
    Gen.main()  
