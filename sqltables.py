#!/usr/bin/env python


db = {}
f = 'MyISAM.txt'


with open(f, 'r') as dictdb:
    for line in dictdb:
        value = line[2]
        key = line.strip()
        #print(line)
        #key, value = line.strip().split(',')
        db.setdefault(key, []).append(value)

for i in db:
    print(db.keys(), db.values())
db.items()
