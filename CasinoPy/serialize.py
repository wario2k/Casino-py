import json

filename = '/Users/aayushshrestha/Casino OPL python/CasinoPy/serial.txt'

with open(filename, mode = 'r') as fh:
    t = json.load(fh)
print(t)