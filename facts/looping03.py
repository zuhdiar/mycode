#!/usr/bin/env python3

import uuid

howmany= int(input("UUIDS to generate? "))
print("generating now")

for i in range(howmany):
    print( uuid.uuid4())

