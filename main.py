#!/usr/bin/env python3
from MacSyntax import CharacterValidate
from MacFormater import *

def settings_display():

    print('\nInvalid MAC addresses won\'t be added to the list')
    print('(a)dd MACs to list')
    print('(l)ist MACs')
    print('(f)ile add MACs')
    print('press \'return/enter\' to escape\n')

def mac_input():

    print('Start adding MAC addresses!')
    while True:
        macadd = input('>').lower()
        if macadd:
            mac = CharacterValidate(macadd)
            mac = mac.validate()
        else:
            break

def mac_output():

    print('--String MACs--')
    string_out = [print(string_mac, end='') for string_mac in EstablishMac.string_macs]
    print('\n--HP MACS--')
    hp_out = [print(hp_mac, end='') for hp_mac in EstablishMac.hp_macs]
    print('\n--Cisco MACs--')
    cisco_out = [print(cisco_mac, end='') for cisco_mac in EstablishMac.cisco_macs]
    print('\n--Hyphen MACS--')
    hyphen_out = [print(hyphen_mac, end='') for hyphen_mac in EstablishMac.hyphen_macs]
    print('\n--Colon MACS--')
    colon_out = [print(colon_mac, end='') for colon_mac in EstablishMac.colon_macs]

def file_output():

    try:
        open('mac-output.txt', 'x')
    except FileExistsError:
        pass
    
    with open('mac-output.txt', 'w') as f:
        f.write('--String MACs--\n')
        f.writelines(mac for mac in EstablishMac.string_macs)
        f.write('\n--HP MACS--\n')
        f.writelines(mac for mac in EstablishMac.hp_macs)
        f.write('\n--Cisco MACs--\n')
        f.writelines(mac for mac in EstablishMac.cisco_macs)
        f.write('\n--Hyphen MACS--\n')
        f.writelines(mac for mac in EstablishMac.hyphen_macs)
        f.write('\n--Colon MACS--\n')
        f.writelines(mac for mac in EstablishMac.colon_macs)
# Main portion of program where we select our options
def main():

    while True:
        settings_display()
        setting_choice = input('>').lower()
        if setting_choice == 'a':
            mac_input()
        elif setting_choice == 'l':
            mac_output()
        elif setting_choice == 'f':
            file_output()
        else:
            break

if __name__ == "__main__":
    main()
