# Package Sorter for Thoughtful's Robotic Automation Factory

This project implements a package sorting function for a robotic automation factory that dispatches packages to the correct stack based on their volume and mass.

## Overview

The robotic arm uses this function to automatically sort packages into three different stacks:
- **STANDARD**: Packages that can be handled normally
- **SPECIAL**: Packages that require special handling
- **REJECTED**: Packages that cannot be processed

## Sorting Rules

### Package Classification

A package is classified as:

- **Bulky** if:
  - Its volume (Width × Height × Length) is ≥ 1,000,000 cm³, OR
  - Any of its dimensions is ≥ 150 cm

- **Heavy** if:
  - Its mass is ≥ 20 kg

### Stack Assignment

- **STANDARD**: Packages that are neither bulky nor heavy
- **SPECIAL**: Packages that are either heavy OR bulky (but not both)
- **REJECTED**: Packages that are both heavy AND bulky

## Function Signature

```python
def sort(width, height, length, mass):
    """
    Sort packages according to their volume and mass.
    
    Args:
        width (float): Width in centimeters
        height (float): Height in centimeters
        length (float): Length in centimeters
        mass (float): Mass in kilograms
    
    Returns:
        str: Stack destination - "STANDARD", "SPECIAL", or "REJECTED"
    """
```

## Usage

### Basic Usage

```python
from package_sorter import sort

# Example: Small, light package
result = sort(10, 10, 10, 5)
print(result)  # Output: "STANDARD"

# Example: Heavy package
result = sort(10, 10, 10, 25)
print(result)  # Output: "SPECIAL"

# Example: Bulky package (by dimension)
result = sort(160, 10, 10, 5)
print(result)  # Output: "SPECIAL"

# Example: Both heavy and bulky
result = sort(160, 10, 10, 25)
print(result)  # Output: "REJECTED"
```

### Running the Tests

The file includes comprehensive test cases that demonstrate all scenarios:

```bash
python package_sorter.py
```

This will run the built-in test suite showing various package types and their expected classifications.

## Test Cases

The implementation includes the following test scenarios:

1. **Standard Package**: Small dimensions, light weight
2. **Heavy Package**: Normal dimensions, heavy weight (≥20 kg)
3. **Bulky by Volume**: Large volume (≥1,000,000 cm³)
4. **Bulky by Dimension**: One dimension ≥150 cm
5. **Rejected Packages**: Both heavy and bulky
6. **Edge Cases**: Packages at exact threshold values

## Requirements

- Python 3.6 or higher
- No external dependencies required


## Implementation Details

The function uses a straightforward approach:

1. Calculate the package volume
2. Check if the package is bulky (volume or dimension criteria)
3. Check if the package is heavy (mass criteria)
4. Apply the sorting logic with conditional statements



## Examples

| Dimensions (cm) | Mass (kg) | Volume (cm³) | Classification | Result |
|-----------------|-----------|--------------|----------------|---------|
| 10×10×10 | 5 | 1,000 | Not bulky, not heavy | STANDARD |
| 10×10×10 | 25 | 1,000 | Not bulky, heavy | SPECIAL |
| 100×100×100 | 5 | 1,000,000 | Bulky (volume), not heavy | SPECIAL |
| 160×10×10 | 5 | 16,000 | Bulky (dimension), not heavy | SPECIAL |
| 100×100×100 | 25 | 1,000,000 | Bulky and heavy | REJECTED |
| 150×10×10 | 20 | 15,000 | Bulky and heavy | REJECTED |

