from time import sleep

import os

print('SO: [{}]'.format(os.name))

sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')