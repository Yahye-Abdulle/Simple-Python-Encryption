'''def encrypt_message():
    file_data = []
    file_name = input('Enter file name: ').strip()
    file = open(file_name+'.txt','r')
    for line in file:
        file_data.append(line)

    print(file_data)'''

import re
import time


def encrypt_message():
    unencrypted_list = []
    encrypted_list_space = []
    file_data = []

    file_name = input('Enter file name: ').strip()
    #user = input('Enter what you want to be encrypted : ')
    offset = int(input('What is the key : '))
    print('== **LEFT OR RIGHT** ==')
    shift = input('Enter type of shift :').lower()

    file = open(file_name + '.txt', 'r')
    for line in file:
        file_data.append(line)

    #user_data = user.strip()
    for i in range(len(file_data)):
        for letter in file_data:
            unencrypted_list.append(ord(file_data[letter][i]))

    for i in range(len(unencrypted_list)):
        if shift == 'left':
            encrypted_letter_left = unencrypted_list[i] - offset
            encrypted_list_space.append(chr(encrypted_letter_left))
        elif shift == 'right':
            encrypted_letter_right = unencrypted_list[i] + offset
            encrypted_list_space.append(chr(encrypted_letter_right))

    encrypted_list = re.sub(' +', ' ', str(encrypted_list_space))

    # print(*unencrypted_list)
    print(*encrypted_list_space)
    print(" ".join(str(encrypted_list)))

    print(file_data)

    menu()


def decrypt_message():
    undecrypted_message = []
    decrypted_message_space = []

    encyrpted_message = input('Enter encrypted message to decrypt : ').strip()
    offset_decrypt = int(input('Enter key used : '))
    shift_decrypt = input('Enter shift used : ').lower()

    for letter_decrypt in encyrpted_message:
        undecrypted_message.append(ord(letter_decrypt))

    for i in range(len(undecrypted_message)):
        if shift_decrypt == 'left':
            undecrypted_letter = undecrypted_message[i] + offset_decrypt
            decrypted_message_space.append(chr(undecrypted_letter))
        elif shift_decrypt == 'right':
            undecrypted_letter = undecrypted_message[i] - offset_decrypt
            decrypted_message_space.append(chr(undecrypted_letter))

    decrypted_message = re.sub(' +', ' ', str(decrypted_message_space))

    # print(*[i for i in decrypted_message if ord(i)])
    print(*decrypted_message)

    menu()


def menu():
    print(' 1. Encrypt\n',
          '2. Decrypt\n',
          '3. Exit')
    option = int(input('Choose option:\n'))
    if option == 1:
        encrypt_message()
    elif option == 2:
        decrypt_message()
    elif option == 3:
        quit()
    else:
        print('Invalid choice')


menu()
