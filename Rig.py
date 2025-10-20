"""
File: Rig.py
Description: This is my rig class. This represents a hackers rig, that can store assets, launch data spikes, take damage,
be repaired, and upgrade its own rig. It handles rig state, level, and stored assets.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset

class Rig:
    # Represents a hackers rig. starts with 2 data spikes and one removable drive.
    def __init__(self, name):
        self.name = name
        self.damage_counter = 0
        self.broken_state = False
        self.level = 0
        # creates 2 data spikes and 1 removable drive
        self.storage = [
            Asset("Data Spike", "Used to attack other rigs, "),
            Asset("Data Spike", "Used to attack other rigs, "),
            Asset("Removable Drive", "Used to extract unsecured assets")]

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_storage(self):
        return self.storage

    def get_broken_state(self):
        return self.broken_state

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        if isinstance(level, int) and level >= 0:
            self.level = level
        else:
            print("Invalid level")

    def set_broken_state(self, broken_state):
        if isinstance(broken_state, bool):
            self.broken_state = broken_state
        else:
            print("Invalid broken state — must be True or False.")


    def repair(self, crypto_token):
        #repairs the rig using a cryptoToken if it is a damaged or broken.
        if not isinstance(crypto_token, Asset) or crypto_token.name != 'CryptoToken':
            print('A valid CryptoToken is required to repair the rig.')
            return

        if self.broken_state == False and self.damage_counter == 0:
            print('No repair is needed!')
            return
        self.damage_counter = 0
        self.broken_state = False
        print(f'{self.name} has been repaired!')

    def upgrade(self, hardware_patch):
        # upgrades the rig using a hardware patch
        if not isinstance(hardware_patch, Asset) or hardware_patch.name != "Hardware Patch":
            print("A valid Hardware Patch is required to upgrade the rig.")
            return

        self.level += 1
        print(f"{self.name} has been upgraded to level {self.level}.")

    def take_hit(self):
        #increases rig damage; breaks if too damaged at that current level.
        self.damage_counter += 1

        # A rig at level 0 will break after two hits.
        if self.damage_counter >= 2 and self.level == 0:
            self.broken_state = True

    def __str__(self):
         if self.broken_state == False:
             self.broken_state = 'Perfect'
         else:
             self.broken_state = 'Broken'
         assets = ""
         if not self.storage:
            assets = "No assets stored"
         else:
             for asset in self.storage:
                 assets += str(asset)
         return (f'The rigs name is:{self.name}\nIts condition is:'f' {self.broken_state}\nIts stored assets are: {assets}')








