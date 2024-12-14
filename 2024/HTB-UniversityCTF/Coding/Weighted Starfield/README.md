# Weighted Starfield
## Description
> The Frontier Starfield signals are destabilized by weighted anomalies. As Space Cowboy, your mission is to restore stability by calculating the maximum stability score from the modified energy signals.
## Overview

The challenge requires calculating the maximum stability score for a starfield by following these steps:

1. **Modification of Signals:** You are given two arrays, `signals` and `weights`. For each element in `signals`, you multiply it by the corresponding element in `weights` to get a new array of modified signals.

2. **Finding Maximum Stability Score:** Once the modified signals are computed, you need to find the maximum product of any contiguous subarray of these modified signals. A subarray is any consecutive sequence of elements in the array.

3. **Output:** Return the maximum product of any contiguous subarray from the modified signals.

### Example Breakdown:

Given the signals array `[1, -2, 3, -4]` and weights array `[2, 3, -1, 4]`:
- Modified signals are calculated as: `[1 * 2, -2 * 3, 3 * -1, -4 * 4]` which results in `[2, -6, -3, -16]`.
- Then, the challenge is to find the subarray with the maximum product:
  - Subarrays and their products:
    - `[2]` → 2
    - `[-6]` → -6
    - `[2, -6]` → -12
    - `[-3, -16]` → 48
  - The maximum product is `48`, which is the final result.

In summary, you are to calculate the modified signals and then find the maximum product of any contiguous subarray within them.

## Solution

```python
def max_stability_score(signals, weights):
    # Calculate the modified signals
    modified_signals = [signals[i] * weights[i] for i in range(len(signals))]
    
    # Initialize the max and min product to the first modified signal
    max_prod = min_prod = modified_signals[0]
    max_score = max_prod
    
    # Iterate over the modified signals
    for i in range(1, len(modified_signals)):
        current_signal = modified_signals[i]
        
        # If the current signal is negative, swap max_prod and min_prod
        if current_signal < 0:
            max_prod, min_prod = min_prod, max_prod
        
        # Update max_prod and min_prod
        max_prod = max(current_signal, max_prod * current_signal)
        min_prod = min(current_signal, min_prod * current_signal)
        
        # Update the global maximum score
        max_score = max(max_score, max_prod)
    
    return max_score

# Input the arrays as strings
signals_str = input()
weights_str = input()

# Sanitize the input by removing unwanted characters like '[' and ','
signals_str = signals_str.replace('[', '').replace(']', '').replace(',', '')
weights_str = weights_str.replace('[', '').replace(']', '').replace(',', '')

# Convert the input strings to lists of integers
signals = list(map(int, signals_str.split()))
weights = list(map(int, weights_str.split()))

# Calculate and print the maximum stability score
print(max_stability_score(signals, weights))
```

## Flag
```
HTB{m1ssi0n_c0mpl3t3d_m4x1mum_5t4b1l1ty_4ch13v3d!_400d3fc23080bc7a1f5cabe19975e138}
```
