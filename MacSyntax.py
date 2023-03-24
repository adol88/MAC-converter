#!/usr/bin/env python3

characters = "abcdef0123456789.-:"
char_list = [char for char in characters]

# Checks the mac-address's length and if it has valid characters.
class CharacterValidate():

    def __init__(self, mac):

        self.mac = mac

    def validate(self):

        if len(self.mac) == 17:

            mac_comp = [c for c in self.mac if char_list.count(c) == 1]

            if ''.join(mac_comp) == self.mac:
                mac = CharacterPosition(self.mac)
                mac.hyphen_hex_place()
            else:
                print(self.mac, 'has invalid characters')

        elif len(self.mac) == 14:
            mac_comp = [c for c in self.mac if char_list[0:17].count(c) == 1]
            
            if ''.join(mac_comp) == self.mac:
                mac = CharacterPosition(self.mac)
                mac.cisco_place()
            else:
                print(self.mac, 'has invalid characters')

        elif len(self.mac) == 13:
            mac_comp = [c for c in self.mac if char_list[0:18].count(c) == 1]

            if ''.join(mac_comp) == self.mac:
                mac = CharacterPosition(self.mac)
                mac.hp_place()
            else:
                print(self.mac, 'has invalid characters')

        elif len(self.mac) == 12:

            mac_comp = [c for c in self.mac if char_list[0:16].count(c) == 1]

            if ''.join(mac_comp) == self.mac:
                mac = CharacterPosition(self.mac)
                mac.string_place()
            else:
                print(self.mac, 'has invalid characters')
        else:
            print('Incorrect Length: ', self.mac)
        
# Verifies that valid characters are in the correct position in the string
class CharacterPosition():

    def __init__(self, mac):

        self.mac = mac

    def hyphen_hex_place(self):

        colon_dash_position = [2,5,8,11,14]
        colon = [pos for pos in colon_dash_position if self.mac[pos] == ":"]
        dash = [pos for pos in colon_dash_position if self.mac[pos] == "-"]

        if colon == colon_dash_position:
            flag = True     # Can probably remove this
            self.mac = self.mac, 'colon'
        elif dash == colon_dash_position:
            flag = True
            self.mac = self.mac, 'dash'
        else:
            flag = False
            print('Invalid mac-address:', self.mac)

        print(self.mac)

    def cisco_place(self):

        decimal_position = [4, 9]
        decimal = [pos for pos in decimal_position if self.mac[pos] == '.']

        if decimal == decimal_position:
            print('Valid Cisco mac address', self.mac)
        else:
            print('Invalid Cisco mac address', self.mac)

    def hp_place(self):
        
        hyphen_position = 6
        if self.mac[hyphen_position] == '-':
            print('Valid HP mac address', self.mac)
        else:
            print('Invalid HP mac address', self.mac)

    def string_place(self):

        print(self.mac)
