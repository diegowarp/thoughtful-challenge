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
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky (volume >= 1,000,000 cm³ or any dimension >= 150 cm)
    is_bulky = volume >= 1000000 or max(width, height, length) >= 150
    
    # Check if package is heavy (mass >= 20 kg)
    is_heavy = mass >= 20
    
    # Sort packages
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"


# Test cases to validate the implementation
if __name__ == "__main__":
    print("Testing package sorting function:")
    print()
    
    # Test case 1: Standard package (not bulky, not heavy)
    result1 = sort(10, 10, 10, 5)
    print(f"Package (10x10x10 cm, 5 kg): {result1}")  # Expected: STANDARD
    
    # Test case 2: Heavy but not bulky
    result2 = sort(10, 10, 10, 25)
    print(f"Package (10x10x10 cm, 25 kg): {result2}")  # Expected: SPECIAL
    
    # Test case 3: Bulky by volume but not heavy
    result3 = sort(100, 100, 100, 5)
    print(f"Package (100x100x100 cm, 5 kg): {result3}")  # Expected: SPECIAL
    
    # Test case 4: Bulky by dimension but not heavy
    result4 = sort(160, 10, 10, 5)
    print(f"Package (160x10x10 cm, 5 kg): {result4}")  # Expected: SPECIAL
    
    # Test case 5: Both heavy and bulky (rejected)
    result5 = sort(100, 100, 100, 25)
    print(f"Package (100x100x100 cm, 25 kg): {result5}")  # Expected: REJECTED
    
    # Test case 6: Both heavy and bulky by dimension (rejected)
    result6 = sort(160, 10, 10, 25)
    print(f"Package (160x10x10 cm, 25 kg): {result6}")  # Expected: REJECTED
    
    # Edge cases
    print("\nEdge cases:")
    result7 = sort(149.9, 10, 10, 19.9)
    print(f"Package (149.9x10x10 cm, 19.9 kg): {result7}")  # Expected: STANDARD
    
    result8 = sort(150, 10, 10, 20)
    print(f"Package (150x10x10 cm, 20 kg): {result8}")  # Expected: REJECTED
    
    result9 = sort(99.9, 99.9, 100.1, 5)  # Volume = 999,799.99 cm³ (not bulky by volume)
    print(f"Package (99.9x99.9x100.1 cm, 5 kg): {result9}")  # Expected: STANDARD
    
    result10 = sort(100, 100, 100, 5)  # Volume = 1,000,000 cm³ (bulky by volume)
    print(f"Package (100x100x100 cm, 5 kg): {result10}")  # Expected: SPECIAL 