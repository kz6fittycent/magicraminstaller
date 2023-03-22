#!/usr/bin/env python3

#IMPORTS
#######################################################
import sys
import time
import threading
import itertools
import os
#######################################################

os.system('clear')

print (50 * '#')
print (50 * '-')
print ("         WELCOME TO MAGIC RAM INSTALLER")
print (50 * '-')
print (50 * '#')
time.sleep(1)
print ("MIT License, v. 1.5")
time.sleep(1)
print()
print()

def main():
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    t_end = time.time() + 15
    ram = str(input("Enter the amount of RAM you want to install:  "))
    print()
    print("Gathering System Information...")
    print()
    time.sleep(5.0)
    print("Wow...your photos are...interesting...")
    print()
    time.sleep(3.0)
    print("Installing RAM Now...")
    print()

    while time.time() < t_end:
          sys.stdout.write(next(spinner))  # write the next character
          sys.stdout.flush()               # flush stdout buffer (actual character display)
          time.sleep(1.0)
          sys.stdout.write('\b') 
            
    else:
          print("Installation Complete!")
          print()
          time.sleep(2.0)
          print("You now have", ram, "of RAM installed.")
          time.sleep(2.0)
          print()
          print("You may want to hide those photos in the future")
          time.sleep(2.0)
          print()
          print("PLEASE REBOOT TO MAKE CHANGES PERMANENT")
          time.sleep(2.0)
          print()
main()

os.system('clear')
