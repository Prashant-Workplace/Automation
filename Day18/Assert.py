def divide(a, b):
    assert b != 0, "The denominator cannot be zero."
    return a / b

print(divide(10, 2))  # This will work fine
print(divide(10, 0))  # This will raise an AssertionError
