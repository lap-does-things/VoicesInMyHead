from os import system,name
from time import sleep
from random import choice
a,n,v = open("voice.voice", mode='r').read().splitlines()[:912][0:],open("voice.voice", mode='r').read().splitlines()[:7694][912:], open("voice.voice", mode='r').read().splitlines()[:8736][7694:]
system('cls' if name == 'nt' else 'clear')
while True:
    voice = "The " +choice(a) + " " + choice(n)+ " " + choice(v)+ "s the " + choice(n)+". "
    for i in range(len(voice)):
        print(voice[i], end='', flush=True)
        sleep(0.1)