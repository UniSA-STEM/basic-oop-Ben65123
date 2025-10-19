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
    # Represents a hackers rig. starts with 2 data spikes and one removable drive.
    def __init__(self, name):
        self.name = name
        self.damage_counter = 0
        self.broken_state = False
        self.level = 0
        # creates 2 data spikes and 1 removable drive
        self.storage = [
            Asset("Data Spike", "Used to attack other rigs"),
            Asset("Data Spike", "Used to attack other rigs"),
            Asset("Removable Drive", "Used to extract unsecured assets")]




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
        #upgrades the rig using a hardware patch from storage
        patch = None
        for asset in self.storage:
            if asset.name == "Hardware Patch":
                patch = asset


        if not patch:
            print(f"{self.name} does not have a Hardware Patch to upgrade.")
            return

        self.storage.remove(patch)
        self.level += 1
        print(f"{self.name} has been upgraded to level {self.level}.")


    def take_hit(self):
        #increases rig damage; breaks if too damaged at that current level.
        self.damage_counter += 1

        # A rig at level 0 will break after two hits.
        if self.damage_counter >= 2 and self.level == 0:
            self.broken_state = True








