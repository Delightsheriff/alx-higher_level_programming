#!/usr/bin/python3
for ascii_code in range(97, 123):
    if ascii_code == 101:
        continue
    elif ascii_code == 113:
        continue
    else:
        print('{:c}'.format(ascii_code), end='')
