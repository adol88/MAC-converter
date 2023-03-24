#!/usr/bin/env python3
from MacSyntax import *

def settings_display():

    print('\nInvalid MAC addresses won\'t be added to the list')
    print('(a)dd MACs to list')
    print('(l)ist MACs')
    print('press \'return/enter\' to escape\n')

def mac_input():

    print('Example mac for testing: ee:b9:64:3e:c3:91') # Remove line when done
    print("Start adding MAC addresses:")
    while True:
        macadd = input("Add Mac> ")
        macadd = macadd.lower()
        if macadd:
            mac = CharLen(macadd)
            mac = mac.length_check()
        else:
            break

# Main portion of program where we select our options
def main():

    while True:
        settings_display()
        setting_choice = input('>').lower()
        if setting_choice == 'a':
            mac_input()
        elif setting_choice == 'l':
            print('Listing mac(s)')
        else:
            print('That choice is not recognized.')

if __name__ == "__main__":
    main()
