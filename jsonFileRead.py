# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 23:26:35 2022

@author: kluleci
"""
import json
with open("customers.json") as customers:
    data=json.load(customers)
    # print(data)
    for x in range (len(data)):
        print(data[x]["id"])
        print(data[x]["name"])
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["address"]["geo"]["lat"])
        print("\n")
        # print(data[0]["username"])
