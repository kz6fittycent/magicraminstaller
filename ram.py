#!/usr/bin/env python3

import sys
import time
import threading
import itertools

print (50 * '#')
print (50 * '-')
print ("         WELCOME TO MAGIC RAM INSTALLER")
print (50 * '-')
print (50 * '#')
time.sleep(1)
print ("MIT License, v. 1.1")
time.sleep(1)
print()


def main():
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    t_end = time.time() + 15
    ram = str(input("Enter the amount of RAM you want to install:  "))
    print()
    print("Getting System Information...")
    print()
    time.sleep(15.0)
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
          print("PLEASE REBOOT TO MAKE CHANGES PERMANENT")
          print()
            print (50 * '#')
            print (50 * '-')
            print ("    THANK YOU FOR USING MAGIC RAM INSTALLER")
            print (50 * '-')
            print (50 * '#')
          
main()
