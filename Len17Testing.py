# A working example of colon and dash testing of the syntax for mac addresses
# Example mac addresses
#mac_address = 'ee:b9:64:3e:c3:91'
#dash_mac = 'ee-b9-64-3e-c3-91'
colon_dash_position = [2,5,8,11,14]     # The index where the colon's or dashes are placed
def position_test():

    colon = [pos for pos in colon_dash_position if mac_address[pos] == ":"]
    dash = [pos for pos in colon_dash_position if mac_address[pos] == "-"]

    if colon == colon_dash_position:
        flag = True
    elif dash == colon_dash_position:
        flag = True
    else:
        flag = False
        print('That is not a valid mac-address:', mac_address)

    if flag:
        print('That is a valid mac:', mac_address)

while True:
    mac_address = input('Enter a mac-address> ')
    position_test()
