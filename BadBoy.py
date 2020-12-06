import subprocess
import os

print("#########################################################")
print("\tWINDOWS PASSWORD EXTRACTOR\t")
print("\tAuthor: sn0d0x_security")
print("\tOnly for Educational Purposes")
print("HAVING A NUMERICAL VALUE IN YOUR USERNAME DOESN'T MAKE YOU LOOK COOL")
print("#########################################################")
print('\n')

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifi = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for i in wifi:
    res  = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    res = [line.split(':')[1][1:-1] for line in res if "Key Content" in line]
    try:
        print(f'Name: {i}, Password: {res[0]}')
    except IndexError:
        print(f'Name: {i}, password: cannot be read')
print(res)