#!/usr/bin/env python3
# MAC-Address generator
# Creates MAC-Addresses in the various different formats
import random

mac_count = int(input('How many mac addresses do you want?> '))

characters = 'abcdef0123456789.-:'
char_list = [char for char in characters]

mac_address_list = []

def string_generator():

    macAddress = []
    counter = 0
    while counter in range(12):
        counter += 1
        macAddress.append(random.choice(char_list[0:16]))
    return macAddress

def cisco_generator():
    
    macAddress = []
    counter = 0
    ciscoDelimeter = [5, 10]
    while counter in range(14):
        counter += 1
        if counter in ciscoDelimeter:
            macAddress.append('.')
        else:
            macAddress.append(random.choice(char_list[0:16]))

    return macAddress

def mac_accumulator():

    counter = 0
    while counter in range(mac_count):
        counter += 1
        macAddress = random.choice(func_list)()
        mac_address_list.append(''.join(macAddress))

func_list = [string_generator, cisco_generator]
mac_accumulator()

for elem in mac_address_list:
    print(elem)
