#!/usr/bin/env python

import os
from sys import argv


script_name, input_file, output_file = argv


def print_line(count):
    print("-" * count)

def check_line(line):
    position = line.tell()
    line = line.readline()
    line.seek(position)
    return line




with open(input_file, 'r') as f, open(output_file, 'a') as w:
    lines = f.readlines()

    no_keys = []
    next_elem = ""
    index = 0
    #while index < len(lines):
    for index, elem in enumerate(lines):
        next_elem = lines[index + 1]
        #    print(index, elem, next_elem)

    #    if "CREATE TABLE" in elem and "PRIMARY KEY" in next_elem:
            # print(f""" Current Element : {elem}.
            #            With PRIMARY_KEY : {next_elem}. """)
    #        pass

        if "CREATE TABLE" in elem and "PRIMARY KEY" not in next_elem:
            print(f""" NO PRIMARY KEY FOR CURRENT ELEMENT :

                            {elem} !!! """)
            elem = elem.strip()
            w.write("{}\n".format(elem))
            no_keys.append(elem)
            print(no_keys)

    for item in no_keys:
        item = item.strip()
        w.write("{}\n".format(item))





#    print(lines[0])
#    print(lines)








#    for line in f:
#        current_line = line
#        #next_line = next(f)
#        print(line)
#        #print(next_line)
#        if "CREATE DATABASE" in line:
#            w.write("PASSING 'CREATE DATABASE' statement for line {}".format(line))
#
#        if ("CREATE TABLE" in line and "CREATE TABLE in "):
#            pass
#        elif "CREATE TABLE" in line:
#                current_line = line
#                next_line = next(f)
#                if "PRIMARY KEY" in next_line:
#                    #print("Table without PRIMARY KEY: {}".format(next_line))
#                    w.write("PASSING TABLE WITH EXISTING PRIMARY KEY  : {0}".format(current_line))
#                    current_line = next_line
#                else:
#                    w.write("Table {0}\n\n\n\n WITHOUT PRIMARY KEY.\n\n\n\n\n\n\n\n".format(current_line))
#                    current_line = next_line
#                    #continue
#
            #    else:
            #        with open(output_file, "a") as w:
            #            print(f"Table without PRIMARY KEY : {next_line} ")
            #            w.write(line, next_line)
