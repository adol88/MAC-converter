#!/usr/bin/env python3

# This class takes a mac from an instantiated object and 
# reformats it. First, it goes through "mac_change" and changes itself into a string, 
# then goes through each function to adjust into the different formats.

class EstablishMac:

    string_macs = []
    hp_macs = []
    cisco_macs = []
    hyphen_macs = []
    colon_macs = []

    def __init__(self, mac):
        self.mac = mac
    
    def change_to_string(mac):

        mac_string = []        # This list allows the mac to change to a string
        no_string_character = ['.', '-', ':']

        # Consolidates none string characters into string format
        for char in mac:
            if char not in no_string_character:
                mac_string.append(char)
        mac = ''.join(mac_string)

        EstablishMac.string_macs.append(mac + '\n')
        return mac

    def change_to_hp(mac):
        
        hp_mac = mac[0:6] + '-' + mac[6:]
        EstablishMac.hp_macs.append(hp_mac + '\n')

    def change_to_cisco(mac):

        cisco_mac = mac[0:4] + '.' + mac[4:8] + '.' + mac[8:]
        EstablishMac.cisco_macs.append(cisco_mac + '\n')

    def change_to_hyphen(mac):

        hyphen_mac = mac[0:2] + '-' + mac[2:4] + '-' + mac[4:6] + '-' + mac[6:8] + '-' \
        + mac[8:10] + '-' + mac[10:]
        EstablishMac.hyphen_macs.append(hyphen_mac + '\n')

    def change_to_colon(mac):

        colon_mac = mac[0:2] + ':' + mac[2:4] + ':' + mac[4:6] + ':' + mac[6:8] + ':' \
        + mac[8:10] + ':' + mac[10:]
        EstablishMac.colon_macs.append(colon_mac + '\n')

    def mac_change(self):

        changing_mac = EstablishMac.change_to_string(self.mac)
        EstablishMac.change_to_hp(changing_mac)
        EstablishMac.change_to_cisco(changing_mac)
        EstablishMac.change_to_hyphen(changing_mac)
        EstablishMac.change_to_colon(changing_mac)
