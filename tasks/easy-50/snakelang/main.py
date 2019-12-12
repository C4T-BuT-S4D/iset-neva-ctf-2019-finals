def decrypt(encoded, key):
    return ''.join( [ chr(((i ^ key) + 10) % 256) for i in encoded] )

def main():
    enc = [235, 213, 224, 234, 198, 218, 145, 218, 226, 156, 220, 238, 233, 226, 156, 221, 223, 157, 211, 234, 158, 226, 209, 216, 221, 233, 145, 211, 196]
    key = int(input("Input one-byte decryption key: "))
    flag = decrypt(enc, key)
    print flag

if __name__ == '__main__':
    main()