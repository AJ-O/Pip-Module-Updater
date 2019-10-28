import os

li = ['asn1crypto', 'astroid', 'certifi']

for l in li:

    os.system('pip3 uninstall ' + l)
    os.system('pip3 install ' + l)

os.system('pip3 list --format=json')
