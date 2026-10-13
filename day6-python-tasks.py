
stock = {
    'LED': 20,
    'RESISTOR': 50,
    'SENSOR': 4
}

requested = ['LED', 'SENSOR', 'SWITCH']

for component in requested:
    quantity = stock.get(component)

    if quantity is not None:
        print(f"{component}: {quantity} available")
    else:
        print(f"{component}: unavailable")


A = {101, 102, 103, 105}
B = {102, 104, 105, 106}

both_courses = sorted(A & B)
only_course_a = sorted(A - B)
either_course = sorted(A | B)

print("Both courses:", both_courses)
print("Only Course A:", only_course_a)
print("Either course:", either_course)


marks = {
    'Arun': 85,
    'Priya': 92,
    'Kavin': 78
}

inverted = {}

for name, mark in marks.items():
    inverted[mark] = name

print(inverted)


names = ['Anu', 'Arun', 'Bala', 'Banu', 'Cathy', 'Asha']

groups = {}

for name in names:
    first_letter = name[0].upper()

    if first_letter not in groups:
        groups[first_letter] = []

    groups[first_letter].append(name)

print(groups)


store_a = {
    'LED': 20,
    'Cable': 10,
    'Board': 3
}

store_b = {
    'Cable': 5,
    'Sensor': 7,
    'LED': 8
}

combined = store_a.copy()

for item, quantity in store_b.items():
    combined[item] = combined.get(item, 0) + quantity

print("Combined inventory:", combined)


sales = {
    'Sensor': [4, 6, 5],
    'Cable': [10, 2, 3],
    'Board': [8, 7],
    'LED': [5, 5, 5]
}

totals = {}

for product, quantities in sales.items():
    totals[product] = sum(quantities)

ranked = sorted(totals.items(), key=lambda item: (-item[1], item[0]))

for product, total in ranked:
    print(f"{product}: {total}")



records = [
    ('D01', 'Lab-A', 'READY'),
    ('D02', 'Lab-B', 'BUSY'),
    ('D01', 'Lab-C', 'MAINTENANCE')
]

devices = {}

for device_id, location, status in records:
    devices[device_id] = {
        'location': location,
        'status': status
    }

print(devices)


permissions = {
    'admin': {'read', 'write', 'delete'},
    'operator': {'read', 'write'},
    'auditor': {'read', 'export'}
}

permission_sets = list(permissions.values())

common_permissions = set.intersection(*permission_sets)
all_permissions = set.union(*permission_sets)

print("Common permissions:", sorted(common_permissions))
print("All permissions:", sorted(all_permissions))


nums = [1, 1, 1]
k = 2

prefix_sum = 0
count = 0
prefix_counts = {0: 1}

for num in nums:
    prefix_sum += num

    required = prefix_sum - k
    count += prefix_counts.get(required, 0)

    prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

print("Count:", count)



s = 'ADOBECODEBANC'
t = 'ABC'

left = 0
required = {c: t.count(c) for c in set(t)}
window = {}
formed = 0
start = 0
min_len = float('inf')

for right, char in enumerate(s):
    window[char] = window.get(char, 0) + 1

    if char in required and window[char] == required[char]:
        formed += 1

    while formed == len(required):
        if right - left + 1 < min_len:
            start = left
            min_len = right - left + 1

        c = s[left]
        window[c] -= 1

        if c in required and window[c] < required[c]:
            formed -= 1

        left += 1

result = '' if min_len == float('inf') else s[start:start + min_len]
print("Minimum window:", repr(result))