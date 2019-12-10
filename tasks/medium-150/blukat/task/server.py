#!/usr/bin/env python3

import string
import random
import base64

flag = b"flag{test}"

class Crypter:
    def __init__(self):
        self.message = b''
        self.token = b''
        self.b64alphabet = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/')

    def random_b64_char(self):
        return self.b64alphabet[random.randint(0, len(self.b64alphabet)) % len(self.b64alphabet)]

    def random_b64(self, length=0, padding=0):
        return ''.join([self.random_b64_char() for _ in range(length)]).encode() + b'=' * padding

    def set_token(self, length=0):
        remainder = length % 3
        b64_length = (length + 2) // 3 * 4
        padding = 0
        if remainder == 1:
            padding = 2
        elif remainder == 2:
            padding = 1

        self.token = base64.b64decode(self.random_b64(b64_length - padding, padding))

    def set_message(self, message):
        self.set_token(len(message))
        self.message = bytes(list(map(lambda x: x[0] ^ x[1], zip(self.token, message))))

    def get_message(self):
        return self.message

    def change_token(self):
        self.message = bytes(list(map(lambda x: x[0] ^ x[1], zip(self.token, self.message))))
        self.set_token(len(self.message))
        self.message = bytes(list(map(lambda x: x[0] ^ x[1], zip(self.token, self.message))))

def print_menu():
    print("####################################")
    print("#        CryptoXor v1.3.3.7        #")
    print("#                                  #")
    print("# 1) Set message                   #")
    print("# 2) Get message                   #")
    print("# 3) Change token                  #")
    print("#                                  #")
    print("####################################")

if __name__ == "__main__":
    c = Crypter()

    while True:
        print_menu()
        option = int(input("Enter option: "))
        if option == 1:
            message = input("Enter your message: ").encode()
            c.set_message(b"Message: [" + message + b"] Flag: [" + flag + b"]")
        elif option == 2:
            print(f"Encoded message: {c.get_message().hex()}")
        elif option == 3:
            c.change_token()
            print("Token changed!")
        else:
            print("Incorrect option!")
