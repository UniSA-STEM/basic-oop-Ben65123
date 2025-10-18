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
    def __init__(self, name):
        self.name = name
        ct_asset = Asset('crpt_token_assset', 'crpt_token_assset_description')
        self.inventory = [ct_asset]
        self.rig = None
        self.trace_level = 0
        self.exposed = False
        self.threshold_amount = 5

        # acquire rig
        self.acquire_a_rig()



    def acquire_a_rig(self, rig= None):

        if self.inventory isinstance(Asset)
            if self.inventory.name == "crypto_token":
                #instantiate Rig object
                rig = Rig()
                self.rig = rig
                # we have consumed one crypto token
                self.inventory=None # can you have more than one crypto token??

        # Allows the hacker to acquire a rig. Costs one CryptoToken. The rig can be passed in or created here.
        if 'CryptoToken' in self.inventory:
            self.inventory.remove('CryptoToken')

            print(f"{self.name} has acquired a rig: {self.rig}")

        else:
            print('f{self.name} does not have enough CryptoTokens to acquire a rig')

    def increase_trace_level(self, amount):
        #Increases trace level; exposes hacker if it exceeds threshold.
        if not isinstance(amount, int): #float?
            print('Trace amount figure must be an integer')
        #elif self.trace_level + amount > self.threshold_amount: # to do fix
            #print('Trace amount figure must be less than the sum of trace_level and amount.')
        else:
            self.trace_level += amount
            print(f' Increasing trace level by {amount}')
            print(f"New trace level is: {self.trace_level}")

        if self.trace_level  > 5:
            self.exposed = True
            print(f"{self.name} has been exposed.")

    def decrease_trace_level(self, amount):
        #Decreases trace level and hides hacker when it is safe again #? not sure method
        if self.trace_level > 0:
            self.trace_level -= amount
        if self.trace_level < 0:
            self.trace_level = 0
        print(f"{self.name} trace level: {self.trace_level}")

        if self.exposed == True and self.trace_level <= 5:
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























