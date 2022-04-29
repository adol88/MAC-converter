# Globals
maclist = []
ciscolist = []
binarylist = []
hexalist = []
# MACinput will check:
# Character length
# If the MAC has valid characters
# If the MAC has periods, colons, dashes or nothing
def MACinput():
    print("Start adding MAC addresses:")
    while True:
        macadd = input("")
        macadd = macadd.lower()
        if macadd:
            charlen(macadd)
        else:
            break
    
# Verifying character length
def charlen(macadd):
    vallen = [12, 14, 17] # Valid lengths for mac-addresses
    if len(macadd) in vallen:
        place(macadd)
    else:
        print("")
        print(macadd, "not the correct length")
# Checks if characters are valid and in the correct places
def place(macadd):
    charls = "abcdef0123456789.-:"
    spl = []
    spl[:0] = macadd
    spl2 = []
    spl2[:0] = charls
    if len(macadd) == 12:
        for x in macadd:
            if spl2.count(x):
                flag = True
            else:
                print(macadd, "incorrect characters found")
                flag = False
                break
        if flag == True:
            macprinter(macadd, spl)
    elif len(macadd) == 14:
        dec1 = spl[4]
        dec2 = spl[9]
        decsum = dec1 + dec2
        oct1 = spl[0:4]
        oct2 = spl[5:9]
        oct3 = spl[10:14]
        octsum = oct1 + oct2 + oct3
        if decsum == "..":
            for x in octsum:
                if spl2.count(x):
                    flag = True
                else:
                    print(macadd, "incorrect characters found")
                    flag = False
                    break
            if flag == True:
                ciscoprinter(macadd, spl)
            else:
                print(macadd, "incorrect period(s) found")

    elif len(macadd) == 17:
        valls = [":::::", "-----"]
        dec1 = spl[2]
        dec2 = spl[5]
        dec3 = spl[8]
        dec4 = spl[11]
        dec5 = spl[14]
        decsum = dec1 + dec2 + dec3 + dec4 + dec5
        oct1 = spl[0:2]
        oct2 = spl[3:5]
        oct3 = spl[6:8]
        oct4 = spl[9:11]
        oct5 = spl[12:14]
        oct6 = spl[15:17]
        octsum = oct1 + oct2 + oct3 + oct4 + oct5 + oct6
# Catches Hex macs   
        if decsum in valls[0]:
            for x in octsum:
                if spl2.count(x):
                    flag = True
                else:
                    print(macadd, "incorrect characters found")
                    flag = False
                    break
            if flag == True:
                hexprinter(macadd, spl)
# Catches Reverse binary macs
        elif decsum in valls[1]:
            for x in octsum:
                if spl2.count(x):
                    flag = True
                else:
                    print(macadd, "incorrect characters found")
                    flag = False
                    break
            if flag == True:
                binaryprinter(macadd, spl)
        else:
            print(macadd, "incorrect colons or dashes found")
# Macs originally input as string will go through here
def macprinter(macadd, spl):
    maclist.append(macadd)
    # Transfer into ciscomac
    spl.insert(4, '.')
    spl.insert(9, '.')
    macadd = ''.join(spl)
    ciscolist.append(macadd)
    spl.remove('.')
    spl.remove('.')
# Transfer into hexmac
    spl.insert(2, ':')
    spl.insert(5, ':')
    spl.insert(8, ':')
    spl.insert(11, ':')
    spl.insert(14, ':')
    macadd = ''.join(spl)
    hexalist.append(macadd)
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
# Transfer into Reverse binary mac
    spl.insert(2, '-')
    spl.insert(5, '-')
    spl.insert(8, '-')
    spl.insert(11, '-')
    spl.insert(14, '-')
    macadd = ''.join(spl)
    binarylist.append(macadd)
# Macs originally input as cisco will go through here
def ciscoprinter(macadd, spl):
    ciscolist.append(macadd)
    spl.remove('.')
    spl.remove('.')
    macadd = ''.join(spl)
    maclist.append(macadd)
# Transfer into hexmac
    spl.insert(2, ':')
    spl.insert(5, ':')
    spl.insert(8, ':')
    spl.insert(11, ':')
    spl.insert(14, ':')
    macadd = ''.join(spl)
    hexalist.append(macadd)
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
# Transfer into Reverse binary mac
    spl.insert(2, '-')
    spl.insert(5, '-')
    spl.insert(8, '-')
    spl.insert(11, '-')
    spl.insert(14, '-')
    macadd = ''.join(spl)
    binarylist.append(macadd)
# Macs originally input as reverse binary will go through here  
def binaryprinter(macadd, spl):
    binarylist.append(macadd)
    spl.remove('-')
    spl.remove('-')
    spl.remove('-')
    spl.remove('-')
    spl.remove('-')
    macadd = ''.join(spl)
    maclist.append(macadd)
# Transfer into ciscomac
    spl.insert(4, '.')
    spl.insert(9, '.')
    macadd = ''.join(spl)
    ciscolist.append(macadd)
    spl.remove('.')
    spl.remove('.')
# Transfer into hexmac
    spl.insert(2, ':')
    spl.insert(5, ':')
    spl.insert(8, ':')
    spl.insert(11, ':')
    spl.insert(14, ':')
    macadd = ''.join(spl)
    hexalist.append(macadd)
# Macs originally input as hexadecimal will go through here
def hexprinter(macadd, spl):
    hexalist.append(macadd)
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
    spl.remove(':')
    macadd = ''.join(spl)
    maclist.append(macadd)
# Transfer into ciscomac
    spl.insert(4, '.')
    spl.insert(9, '.')
    macadd = ''.join(spl)
    ciscolist.append(macadd)
    spl.remove('.')
    spl.remove('.')
# Transfer into binarymac
    spl.insert(2, '-')
    spl.insert(5, '-')
    spl.insert(8, '-')
    spl.insert(11, '-')
    spl.insert(14, '-')
    macadd = ''.join(spl)
    binarylist.append(macadd)

# Main portion of the program; Gives option settings
while True:
    print("Invalid MACs won't be added to the list")
    print("a = Add MACs to list\nl = List MACs\nPress return to escape")
    choice = input("")
    choice = choice.lower()
    if choice == "a":
        MACinput()
    elif choice == "l":
        print("--String--")
        print(*maclist, sep="\n")
        print("")
        print("--Cisco--")
        print(*ciscolist, sep="\n")
        print("")
        print("--Colon-Hexadecimal--")
        print(*hexalist, sep="\n")
        print("")
        print("--Hyphen-Hexadecimal--")
        print(*binarylist, sep="\n")
        input()
    else:
        break
