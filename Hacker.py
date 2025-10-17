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
        # Allows the hacker to acquire a rig. Costs one CryptoToken. The rig can be passed in or created here.
        if 'CryptoToken' in self.inventory:
            self.inventory.remove('CryptoToken')
            self.rig = rig
            print(f"{self.name} has acquired a rig: {self.rig}")

        else:
            print('f{self.name} does not have enough CryptoTokens to acquire a rig')

    def increase_trace_level(self, amount):
        #Increases trace level; exposes hacker if it exceeds threshold.
        self.trace_level += amount
        print(f"{self.name} trace level: {self.trace_level}")

        if self.trace_level > 5:
            self.exposed = True
            print(f"{self.name} has been exposed.")

    def decrease_trace_level(self, amount):
        #Decreases trace level and hides hacker when it is safe again
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
        if 'Data Spike' in self.rig.storage:
            self.rig.storage.remove('Data Spike')
            target_rig.damage += 1
            print('f{self.name} has damaged {target_rig} with a Data Spike')
        else:
            print(f'{self.name} does not have enough Data Spike')

    def extract_unsecured_assets(self, target_rig):

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




















