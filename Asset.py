
#File: Asset.py
#Description: This is my asset classes. It defines the assets used by hackers and rigs. These asset objects include data spikes,
#crypto tokens, removable drive and security chips.

#Author: Benjamin sienicki
#ID: 110442676
#Username: sieby003
#This is my own work as defined by the University's Academic Misconduct Policy.

class Asset:
    # The Asset class stores an asset’s name and description and tracks if it is encrypted or not.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False
    def __str__(self):
        if self.encrypted:
            return f'{self.name}: {self.description} [Encrypted]'
        else:
            return f'{self.name}: {self.description}'

