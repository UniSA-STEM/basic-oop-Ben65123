"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Benjamin sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self, name,):
        self.name = name
        self.inventory = ['CryptoToken']
        self.rig = None
        self.trace_level = 0
        self.exposed = False

    def acquire_a_rig(self, rig= None):
        if 'CryptoToken' in self.inventory:
            self.inventory.remove('CryptoToken')
            self.rig = rig
            print(f"{self.name} has acquired a rig: {self.rig}")

        else:
            print('f{self.name} does not have enough CryptoTokens to acquire a rig')

    def increase_trace_level(self, amount):
        self.trace_level += amount
        print(f"{self.name} trace level: {self.trace_level}")












