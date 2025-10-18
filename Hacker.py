"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Benjamin sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

class Hacker:
    #The Hacker class represents a hacker with a name, an inventory, a rig, and a trace level.
    def __init__(self, name):
        self.name = name
        crypto_token = Asset("CryptoToken", "Used to buy or repair rigs")
        self.inventory = [crypto_token]
        self.rig = None
        self.trace_level = 0
        self.exposed = False




    def acquire_a_rig(self, rig= None):
        #Allows hacker to acquire a rig.
        #Look through inventory to find crypto token.
        found_token = None
        for item in self.inventory:
            if isinstance(item, Asset) and item.name == "CryptoToken":
                found_token = item
                break

        #If no token can be found, cant get a rig.

        if found_token is None:
            print('f{self.name} does not have enough CryptoTokens to acquire a rig')
            return
        #Use one crypto token
        self.inventory.remove(found_token)

        # If a rig is passed in use it if not create a new one.
        if rig:
            self.rig = rig
        else:
            self.rig = Rig(f"{self.name}'s Rig")
        print(f"{self.name} has acquired a rig: {self.rig}")

    def increase_trace_level(self, amount=1):
        #Increases trace level; exposes hacker if it exceeds threshold.
        if not isinstance(amount, int): #float?
            print("Trace amount must be an integer.")
            return

        if amount < 0:
            print("Trace amount must be zero or positive.")
            return

        self.trace_level += amount
        print(f' Increasing trace level by {amount}')
        print(f"New trace level is: {self.trace_level}")

        if self.trace_level  > 5:
            self.exposed = True
            print(f"{self.name} has been exposed.")

    def decrease_trace_level(self, amount=1):
        # Decreases trace level. If trace falls to 5 or below while exposed, hide the hacker.
        if not isinstance(amount, int):
            print("Trace amount must be an integer.")
            return

        if amount < 0:
            print("Trace amount must be zero or positive.")
            return

        if self.trace_level > 0:
            self.trace_level -= amount
            if self.trace_level < 0:
                self.trace_level = 0

        print(f"{self.name} trace level: {self.trace_level}")

        if self.exposed and self.trace_level <= 5:
            self.exposed = False
            print(f"{self.name} has been hidden.")

    def launch_data_spikes(self, target_rig):
        # launches data spikes at other rigs.
        if 'Data Spike' in target_rig.storage:
            self.rig.storage.remove('Data Spike')
            target_rig.damage += 1
            print('f{self.name} has damaged {target_rig} with a Data Spike')
        else:
            print(f'{self.name} does not have enough Data Spike')

    def extract_unsecured_assets(self, target_rig):
        #extracts all unencrypted data from a broken target rig

        if not self.rig:
            print(f"{self.name} has no rig to extract with.")
            return

        if target_rig.damage < target_rig.max_damage:
            print(f"{target_rig.name} is not broken; extraction not allowed.")
            return

        if 'Removable Drive' not in self.rig.storage:
            print(f"{self.name} does not have a Removable Drive.")
            return

        self.rig.storage.remove('Removable Drive')
        print(f"{self.name} used a Removable Drive to extract assets from {target_rig.name}.")

        for asset in list(target_rig.storage):
            if not asset.encrypted:
                self.inventory.append(asset)
                target_rig.storage.remove(asset)

        target_rig.storage.clear()

        print(f"{self.name} extracted items: {self.inventory}")

    def __str__(self):
        return f"Hacker object\n{self.name} "# To do add rest of fields'

     # def encrypt_assets(self, assets):
#
#
#























