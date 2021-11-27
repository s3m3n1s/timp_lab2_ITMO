#!/bin/python
from os import path
import json
import time
start = time.time()


def add_new_name(name):
    with open(path.expanduser('~') + '/.co', 'r') as co:
        count, time1 = co.readlines()
        count = int(count)
        time1 = int(time1)
        if count<=0:
            print("Licence expire. Please buy or deinstall it")
            return 1
    if time.time()-start > time1:
        print("Licence expire. Please buy or deinstall it")
        return 1
    with open(path.expanduser('~') + '/.co', 'w') as co:
        co.writelines([str(count-1), "\n30"])
    if time.time()-start > time1:
        print("Licence expire. Please buy or deinstall it")
        return 1
    with open(path.expanduser('~') + '/.namesaver/names.json', 'r') as file:
        a = json.load(file)
    if time.time()-start > time1:
        print("Licence expire. Please buy or deinstall it")
        return 1
    if name in a['names']:
        print('Sorry, we know you')
    else:
        a['names'].append(name)
        with open(path.expanduser('~') + '/.namesaver/names.json', 'w') as file:
            json.dump(a, file)


add_new_name(input("Введите имя: "))
