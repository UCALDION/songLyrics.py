import sys
from time import sleep
import time 

def print_song():
    lines = [
        ("Cross my heart, hope to die", 0.06),
        ("To my lover, I'd never lie", 0.07),
        ("He said 'be true,' I swear I'll try", 0.07),
        ("In the end, it's him and I", 0.06),
        ("He's out his head, I'm out my mind", 0.08),
        ("We got that love, the crazy kind", 0.07),
        ("I am his, and he is mine", 0.07),
        ("In the end, it's him and I, him and I", 0.08),
    ]


    delays = [0.5, 0.6, 0.6, 0.6, 0.8, 0.8, 0.7, 0.8]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_song()