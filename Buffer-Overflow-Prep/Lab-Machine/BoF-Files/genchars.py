#!/usr/bin/python3

import sys

# 0 - 256 is 0x00000000 - 0xffffffff
for i in range(1,256):
    sys.stdout.write("\\x" + '{:02x}'.format(i))


