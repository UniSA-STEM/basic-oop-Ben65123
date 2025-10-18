"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


from Hacker import Hacker
from Asset import Asset

if __name__ == '__main__':

    # create hack
    hack = Hacker('bob')
    a = Asset('a1', 'a2' )
    print(a)

    h1 = Hacker('bob')
    crpt_token_assset = Asset('crpt_token_assset', 'crpt_token_assset')
    h1.inventory



    #test acquire rig
    # hack.acquire_a_rig('bobs rig')
    # print(hack)
    #
    # hack.increase_trace_level('hey')
    #
    # hack.decrease_trace_level(-1)




