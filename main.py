#!/usr/bin/env python3
from MacSyntax import CharacterValidate
from MacFormater import *

def settings_display():

    print('\nInvalid MAC addresses won\'t be added to the list')
    print('(a)dd MACs to list')
    print('(l)ist MACs')
    print('press \'return/enter\' to escape\n')

def mac_input():

    print("Start adding MAC addresses:")
    while True:
        macadd = input("Add Mac> ")
        macadd = macadd.lower()
        if macadd:
            mac = CharacterValidate(macadd)
            mac = mac.validate()
        else:
            break

def mac_output():

    print('\n--String MACs--')
    string_out = [print(string_mac) for string_mac in EstablishMac.string_macs]
    print('\n--HP MACS--')
    hp_out = [print(hp_mac) for hp_mac in EstablishMac.hp_macs]
    print('\n--Cisco MACs--')
    cisco_out = [print(cisco_mac) for cisco_mac in EstablishMac.cisco_macs]
    print('\n--Hyphen MACS--')
    hyphen_out = [print(hyphen_mac) for hyphen_mac in EstablishMac.hyphen_macs]
    print('\n--Colon MACS--')
    colon_out = [print(colon_mac) for colon_mac in EstablishMac.colon_macs]

# Main portion of program where we select our options
def main():

    while True:
        settings_display()
        setting_choice = input('>').lower()
        if setting_choice == 'a':
            mac_input()
        elif setting_choice == 'l':
            mac_output()
        else:
            break

if __name__ == "__main__":
    main()
