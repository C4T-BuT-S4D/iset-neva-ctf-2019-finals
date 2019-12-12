from base64 import b32encode, b64encode, b85encode
from hashlib import md5
from binascii import hexlify
import random
import string

def random_string(length = 10):
    alphabet = string.ascii_lowercase
    return ''.join(random.choice(alphabet) for i in range(length))

def task_text(encoding):
    return 'Please provide decoded {} data'.format(encoding)

def gen_encoded(encoding):
    message = random_string(10)
    encoded = ''
    if encoding == 'hex':
        encoded = hexlify(message.encode()).decode()
    elif encoding == 'base32':
        encoded = b32encode(message.encode()).decode()
    elif encoding == 'base64':
        encoded = b64encode(message.encode()).decode()
    else:
        nums = [ord(i) for i in string.ascii_lowercase]
        message = chr(random.choice(nums))
        encoded = md5(message.encode()).hexdigest()

    return message, encoded

def main():
    flag = 'flag{brut3f0rc3_g0d}'
    encodings = ['hex', 'base32', 'base64', 'base64', 'md5, one byte message']
    amount = [2, 2, 2, 2, 2]
    done = 0
    while done != sum(amount):
        current_encoding = encodings[done // 2]
        ans, enc = gen_encoded(current_encoding)
        print(task_text(current_encoding))
        print(enc)
        user_ans = input()
        if user_ans != ans:
            break
        print('Correct!')
        done += 1
    if done != sum(amount):
        print('Try harder')
    else:
        print(flag)

if __name__ == '__main__':
    main()