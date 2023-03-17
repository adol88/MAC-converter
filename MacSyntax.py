#!/usr/bin/env python3

# Checks if the mac length is valid
class CharLen:
    
    def __init__(self, mac):

        self.mac = mac

    def length_check(self):

        valid_lengths = [12, 14, 17]

        if len(self.mac) in valid_lengths:
            mac = CharacterValidate(self.mac)
            mac = mac.validate()
        else:
            print('\n', self.mac, 'is not the correct length')

# Checks if the mac has valid characters
class CharacterValidate():

    characters = "abcdef0123456789.-:"
    char_list = [char for char in characters]    # Lazy way of turning 'characters' into a list

    def __init__(self, mac):

        self.mac = mac

    def validate(self):
        # Need to rewrite the validate function to incorporate the other mac lengths
        if len(self.mac) == 17:
            for c in self.mac:
                if CharacterValidate.char_list.count(c):
                    flag = True
                else:
                    flag = False
                    break
            self.mac = self.mac, 'colon_dash'

        elif len(self.mac) == 14:
            print(self.mac)         # Placeholder

        elif len(self.mac) == 12:
            for c in self.mac:
                if CharacterValidate.char_list[0:16].count(c):
                    flag = True
                else:
                    flag = False
                    break
            self.mac = self.mac, 'string'

        if flag:
            mac = MacType(self.mac)
            mac = mac.mac_type()
        else:
            print('Invalid characters found in:', self.mac[0])

# Determines the type of mac-address
class MacType:
        
    def __init__(self, mac):

        self.mac = mac
        
    def mac_type(self):
        print('Determining mac-type...', self.mac[0]) # Remove this line when done
        mac = CharacterPosition(self.mac[0])
        if self.mac[1] == 'string':
            mac.string_place()
        elif self.mac[1] == 'colon_dash':
            mac.colon_hex_place()
        
# Verifies that valid characters are in the correct position in the string
class CharacterPosition():

    def __init__(self, mac):

        self.mac = mac

    def string_place(self):

        for c in self.mac:
            if c in CharacterValidate.characters[0:16]:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            print('Valid MAC-Address: ', self.mac)
        else:
            print('Invalid MAC-Address: ', self.mac)

    def hp_place(self):
        pass

    def cisco_place(self):
        pass

    def colon_hex_place(self):

        colon_dash_position = [2,5,8,11,14]
        colon = [pos for pos in colon_dash_position if self.mac[pos] == ":"]
        dash = [pos for pos in colon_dash_position if self.mac[pos] == "-"]

        if colon == colon_dash_position:
            flag = True
            self.mac = self.mac[0], 'colon'
        elif dash == colon_dash_position:
            flag = True
            self.mac = self.mac[0], 'dash'
        else:
            flag = False
            print('Invalid mac-address:', self.mac)
        # This should now be ready to pass into MacPrinter

    def hyphen_hex_place(self):
        pass
