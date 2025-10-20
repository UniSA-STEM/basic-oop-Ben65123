"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Rig import Rig
from Asset import Asset
from Hacker import Hacker


if __name__ == '__main__':

    # Create a hacker
    print("=== Creating Hacker ===")
    hacker = Hacker("Neo")
    print(hacker)
    print()

    # Acquire a rig
    print("=== Acquiring Rig ===")
    hacker.acquire_a_rig()
    print(hacker)
    print()

    # Test storing and retrieving assets
    print("=== Testing Store and Retrieve Assets ===")
    drive = Asset("Removable Drive", "Used to extract assets")
    hacker.inventory.append(drive)
    hacker.store_assets(drive)
    hacker.retrieve_assets(drive)
    print()

    # Test upgrading rig
    print("=== Testing Rig Upgrade ===")
    patch = Asset("Hardware Patch", "Used to upgrade rigs")
    hacker.inventory.append(patch)
    hacker.upgrade_rig()
    print()

    # Test encrypt/decrypt assets
    print("=== Testing Encryption and Decryption ===")
    chip = Asset("Security Chip", "Used to encrypt assets")
    file1 = Asset("File", "Important data")
    hacker.inventory.append(chip)
    hacker.inventory.append(file1)
    hacker.encrypt_assets([file1])
    hacker.decrypt_assets([file1])
    print()

    # Test damage and repair
    print("=== Testing Rig Damage and Repair ===")
    hacker.rig.take_hit()
    hacker.rig.take_hit()
    token = Asset("CryptoToken", "Used to buy or repair rigs")
    hacker.rig.repair(token)
    print()

    # Show final state
    print("=== Final Hacker State ===")
    print(hacker)
    print(hacker.rig)











# Testing hacker


    # hack = Hacker('bob')
    # a = Asset('a1', 'a2' )
    # print(a)
    # h1 = Hacker('tom')
    # crpt_token_assset = Asset('crpt_token_assset', 'crpt_token_assset')
    # h1.inventory
    #Testing hacker methods


    # hack.acquire_a_rig('bobs rig')
    # print(hack)
    # hack.increase_trace_level('hey')
    # hack.decrease_trace_level(-1)

    #Testing hacker and rig after a few imporvements.
    # hacker1 = Hacker("Neo")
    # hacker2 = Hacker("Trinity")
    #
    # rig_target = Rig("Matrix Rig")
    #
    # # print(hacker1)
    # # print(hacker2)
    #
    # hacker1.rig = Rig("Neo Rig")
    # hacker1.rig.data_spike_counter = 2
    # hacker1.rig.storage = [Asset("Removable Drive", "Used for extraction")]
    # rig_target.storage = [Asset("Data File", "Sensitive info")]
    #
    # print("\n--- Trace Level Tests ---")
    # hacker1.increase_trace_level(3)
    # hacker1.increase_trace_level(3)
    # hacker1.decrease_trace_level(2)
    # hacker1.decrease_trace_level(2)
    #
    #
    # print("\n--- Data Spike Tests ---")
    # hacker1.launch_data_spikes(rig_target)
    # hacker1.launch_data_spikes(rig_target)
    # print(f"{rig_target.name} damage_counter: {rig_target.damage_counter}, broken_state: {rig_target.broken_state}")

    #Test for upgrade rig before adding hardware patch to storage.
    # patch = Asset("Hardware Patch", "Upgrades the rig to a higher level")
    #
    #my_rig = Rig("R1")
    #
    # print("Before upgrade:")
    # print(my_rig.level)
    # my_rig.upgrade("Hardware Patch")
    # print("After upgrade:")
    # print(my_rig.level)
    #
    # #After adding hardware patch to storage should upgrade the level now.
    #
    # my_rig.storage.append(patch)
    # my_rig.upgrade("Hardware Patch")
    # print("After upgrade:")
    # print(my_rig.level)

    #tested get hit method
    # print("Before hit:")
    # print(f"Damage: {my_rig.damage_counter}, Broken: {my_rig.broken_state}")
    #
    # my_rig.take_hit()
    # print("After 1st hit:")
    # print(f"Damage: {my_rig.damage_counter}, Broken: {my_rig.broken_state}")
    #
    # my_rig.take_hit()
    # print("After 2nd hit:")
    # print(f"Damage: {my_rig.damage_counter}, Broken: {my_rig.broken_state}")

    # my_rig.broken_state = True
    # print(my_rig)


















