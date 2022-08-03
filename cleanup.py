import os
from os.path import expanduser
import sys

home = expanduser("~")

# Change these as you wish
dangertypes = ['zip', '7z', 'rar']
filetypes = ['exe', 'msi', 'zip']
directory = f'{home}/Downloads'

directorylist = os.listdir(f'{home}/{directory}')

print("Here is a list of files to be deleted:\n")

dangerlist = []
normallist = []

for filename in filetypes:
    if os.path.isdir(f'{directory}/{filename}'):
        continue
    type1 = f'.{filename[-3]}'
    type2 = filename[-1]
    for file in directorylist:
        fileex = file.split('.')[-1]
        if fileex in dangertypes and file not in dangerlist:
            if fileex in filetypes:
                print(f'> [!] {file}')
                dangerlist.append(file)
        elif fileex in filetypes and file not in normallist and file not in dangerlist:
            print(f'> {file}')
            normallist.append(file)
            dangerlist.append(file)

print("\nThe danger list deletes ALL the files listed.\nThe normal list deletes the files without the '[!]'.\n")
validresponses = ['d', 'n', 'q']
inp = ''

while inp not in validresponses:
    inp = input('Type \'d\' to delete everything on the danger list.\nType \'n\' to delete everything on the normal '
                'list.\nType \'q\' to quit the program.\n> ')

print()

if inp == 'q':
    sys.exit()
elif inp == 'n':
    for file in normallist:
        try:
            os.remove(f'{directory}/{file}')
            print(f'[✓] {file}')
        except OSError:
            print(f'[x] {file}')
elif inp == 'd':
    for file in dangerlist:
        try:
            os.remove(f'{directory}/{file}')
            print(f'[✓] {file}')
        except OSError:
            print(f'[x] {file}')
print("\nDone!")
sys.exit()
