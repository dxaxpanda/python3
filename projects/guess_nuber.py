import random



## declare a counter for the numbers of attempts
counter = 0



def get_username():# ask player's name
    username = input("""
        Hello fellow player,
        welcome to this game.
        We are now wondering what your name is ? """)
    return username

def get_unknown(top, bottom): # get a random number

    unknown = random.randint(top, bottom)
    return unknown

name = get_unknown(1, 2000)
print(name)
if name == 'test':
    print(f"your usename is {name}")
elif name == 'wesh':
    print(f"your username is {name}")
else:
    print("LOOSE")
