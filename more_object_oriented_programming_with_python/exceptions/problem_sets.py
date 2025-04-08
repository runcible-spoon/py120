numbers = [1, 2, 3, 4, 5]

def lbyl():
    return None if len(numbers) < 6 else numbers[5]

def afnp():
    try:
        return numbers[5]
    except IndexError:
        return None

print(lbyl())
print(afnp())
