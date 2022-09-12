#!/usr/bin/env python

import os
import sys
import random
import string

# Clear console
if os.name == 'nt': #windows
    os.system('cls')
else: #'posix', for linux, mac
    os.system('clear')

# Command line arguments
sys_argv = lambda i, d=-1: int(sys.argv[i]) if len(sys.argv) >= i+1 and sys.argv[i].lstrip('-').isdigit() else d


def random_01():
    x = input('String = ')
    for i in range(0,10):
        y = ''.join(random.sample(x,len(x)))
        print(y)


def random_02():
    for i in range(0,65):
        m = random.randint(6, 7)
        d = random.randint(1, 20)
        diff = random.randint(1, 10)
        date1 = "2018/07/"+str(d).zfill(2)
        date2 = "2018/07/"+str(d+diff).zfill(2)
        print(date1+'\t'+date2)


def random_03():
    for i in range(0,25):
        if i<6:
            n = random.uniform(0.199, 0.3)
        elif i>=6 and i<12:
            n = random.uniform(-0.487,0.199)
        elif i>=12 and i<18:
            n = random.uniform(-1.174,-0.487)
        else:
            n = random.uniform(-2, -1.174)
        print(n)


def generate_random_string(length):
    characters = string.digits
    characters += string.ascii_letters
    return ''.join(random.choice(characters) for i in range(length))


def random_password():
    length = int(input('length = '))
    num = int(input('times = '))
    letters = string.ascii_letters + string.digits
    with open('random.txt', mode='w') as fw:
        passwords = []
        for n in range(0,num):
            result = ''.join(random.choice(letters) for i in range(length))
            if result not in passwords:
                passwords.append(result)
                fw.write(result + '\n')


def generate_password():
    length = int(input('length = '))
    print(generate_random_string(length))


def do_something():
    # print(generate_random_string(20))
    print('random ip')
    ip = '%d.%d.%d.%d' % (random.randint(0,256), random.randint(0,256), random.randint(0,256), random.randint(0,256))
    print(ip)


def main():
    actions = [
        {
            "desc": "Generate password",
            "action": generate_password
        },
        {
            "desc": "Random password",
            "action": random_password
        },
        {
            "desc": "Do something",
            "action": do_something
        },
    ]
    arg1 = sys_argv(1,-1)
    if arg1 in range(1, len(actions)+1):
        actions[arg1-1]['action']()
    else:
        for i in range(0,len(actions)):
            print('{0:3d}. {1:s}'.format(i+1, actions[i]['desc']))
        try:
            print("")
            option = int(input('Choose action: '))
            print("")
            if option in range(1, len(actions)+1):
                actions[option-1]['action']()
            else:
                print('Invalid choice')
        except ValueError:
            print('\nInvalid input')


if __name__ == '__main__':
    main()
