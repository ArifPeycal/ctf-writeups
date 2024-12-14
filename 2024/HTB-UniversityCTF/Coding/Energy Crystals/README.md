# Energy Crystals
## Description
> The ancient Starry Spur has been recovered, but its energy matrix remains dormant. As Space Cowboy, your task is to awaken its power by calculating the combinations of energy crystals that match the required energy level.

## Overview
Your mission is to calculate the number of ways to combine these crystals to match the required energy level. Each crystal can be used an unlimited number of times, but the combinations must add up to the exact target energy.

Example
Input
Example 1:
Energy Crystals: [1, 2, 3]
Target Energy: 4

Example 2:
Energy Crystals: [2, 5, 3, 6]
Target Energy: 10

Output
Example 1 Output: 4
Explanation: There are 4 distinct ways to combine the crystals to reach the target energy level of 4:

1 + 1 + 1 + 1
1 + 1 + 2
2 + 2
1 + 3
Example 2 Output: 5
Explanation: There are 5 distinct ways to combine the crystals to reach the target energy level of 10:

2 + 2 + 2 + 2 + 2
2 + 2 + 2 + 2 + 2 + 2 + 3
2 + 2 + 2 + 6
5 + 5
2 + 3 + 5
Each combination adds up to the target energy level of 10. As before, the order of the crystals does not matter.

## Solution
```python
# Input energy crystals and target energy as strings
energy_crystals = input()  # Input as a string
target_energy = input()  # Input as a string

energy_crystals = energy_crystals.replace('[', '').replace(']', '').replace(',', ' ')
target_energy = target_energy.strip()

try:
    # Convert inputs to proper data types
    energy_crystals = list(map(int, energy_crystals.split()))  # Convert to a list of integers
    target_energy = int(target_energy)  # Convert to an integer

    # Function to calculate the number of ways
    def count_combinations(energy_crystals, target_energy):
        # Initialize the DP array with zeros, and set dp[0] = 1
        dp = [0] * (target_energy + 1)
        dp[0] = 1

        # Update DP array for each crystal
        for crystal in energy_crystals:
            for j in range(crystal, target_energy + 1):
                dp[j] += dp[j - crystal]

        return dp[target_energy]

    # Calculate and print the number of ways
    print(count_combinations(energy_crystals, target_energy))

except ValueError:
    print("Invalid input! Please enter energy crystals as integers and target energy as a single integer.")
```
## Flag
```
HTB{3n34gy_m4tr1x_act1v4t3d_w3_4r3_s4v3d!_15bf7d54c1bdc5d1c0ed6d652db78dc9}
```
