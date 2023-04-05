#!/usr/bin/env python3

# If we want to specify which macs to print out, perhaps we can
# consolidate every mactype list into an even larger list
# then, exclude/include as necessary
string_macs = []
hp_macs = []
cisco_macs = []
hyphen_macs = []
colon_macs = []

def change_to_string(mac):

    mac_string = []        # This list allows the mac to change to a string
    no_string_character = ['.', '-', ':']

    # Consolidates none string characters into string format
    for char in mac:
        if char not in no_string_character:
            mac_string.append(char)
    mac = ''.join(mac_string)

    string_macs.append(mac)
    return mac

def change_to_hp(mac):
    
    hp_mac = mac[0:6] + '-' + mac[6:]
    hp_macs.append(hp_mac)

def change_to_cisco(mac):

    cisco_mac = mac[0:4] + '.' + mac[4:8] + '.' + mac[8:]
    cisco_macs.append(cisco_mac)

def change_to_hyphen(mac):

    hyphen_mac = mac[0:2] + '-' + mac[2:4] + '-' + mac[4:6] + '-' + mac[6:8] + '-' \
    + mac[8:10] + '-' + mac[10:]
    hyphen_macs.append(hyphen_mac)

def change_to_colon(mac):

    colon_mac = mac[0:2] + ':' + mac[2:4] + ':' + mac[4:6] + ':' + mac[6:8] + ':' \
    + mac[8:10] + ':' + mac[10:]
    colon_macs.append(colon_mac)

class EstablishMac:

    def __init__(self, mac):
        self.mac = mac
    
    def mac_change(self):

        mac = self.mac[0]       # Extract mac from its tuple

        changing_mac = change_to_string(mac)
        change_to_hp(changing_mac)
        change_to_cisco(changing_mac)
        change_to_hyphen(changing_mac)
        change_to_colon(changing_mac)

        print(string_macs)      # Remove these lines when done
        print(hp_macs)
        print(cisco_macs)
        print(hyphen_macs)
        print(colon_macs)
