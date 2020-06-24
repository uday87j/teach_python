#!python3

#
# This file is _aware_ that there are 200 people in the file called `names`
# This script will create a bitmap to represent the social netork of people in `names`
#

import sys
import os
import random
import functools

def gen_network(person: str) -> str:
    """
    Generates a bitmap to indicate whether person is connected to each of the 200 arbitrary persons
    Returns a string bitmap
    """
    bitmap: str = ""
    for n in range(0, 200):
        bitmap = "".join([bitmap, str(random.randint(0, 1))])

    assert len(bitmap) == 200
    return bitmap

def connect_person_to_self(cxn: str, person_index: int) -> str:
    """
    cxn should represent person's network as a bitmap of 0s and 1s
    """
    assert person_index < len(cxn)
    alpha_chars = list(
            filter(lambda x: x.isalpha(), cxn)
            )
    assert len(alpha_chars) == 0

    return "".join([cxn[:person_index], "1", cxn[person_index + 1:]])

def gen_name_network(name: str, index: int) -> str:
    """
    Return a string with name and network separated by whitespace
    """
    cxn: str = connect_person_to_self(
            gen_network(name),
            index
            )
    return " ".join([name, cxn])

def remove_header(l: list) -> list:
    """
    Header is at index 0
    """
    assert len(l) > 0
    header = l[0]
    del l[0]
    return header

def main():
    lines: list = []

    with open(os.sep.join([os.getcwd(), "names"])) as fd:
        lines = fd.read().splitlines()

    header: str = remove_header(lines)

    for index,name in enumerate(lines):
        lines[index] = gen_name_network(name, index)

    with open(os.sep.join([os.getcwd(), "network"]), 'w') as fw:
        fw.write(header)
        for line in lines:
            fw.write('\n'.join(["", line]))

if __name__ == '__main__':
    main()
