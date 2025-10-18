"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.

"""

from Asset import Asset

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage_counter = 0
        self.broken_state = False
        self.storage = None
        self.data_spike_counter = 2
        self.removable_drive_counter = 1
        self.level = 0

        # create two data spike objects
        ds1 = Asset("ds1", "dataspike object")
        ds2 = Asset("ds2", "dataspike object")
        self.storage - [ds1, ds2]

    def repair(self, crypto_token): #? what to do with crypto token
        if not isinstance(crypto_token, int):
            print('CryptoToken must be an int')
        else:
            if self.broken_state == False and self.damage_counter == 0:
                print('No repair is needed!')
            else:
                self.damage_counter == 0
                self.broken_state = False

    def upgrade(self, hardware_patch):
        self.level += 1

    def take_hit(self):
        self.damage_counter += 1
        if self.damage_counter == 2 and self.level == 0:
            self.broken_state = True

    def generate_assets(self
        pass):






