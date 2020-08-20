d = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}

total = 0

for value in d.values():
    if type(value) is int:
        total += value

print(total)
