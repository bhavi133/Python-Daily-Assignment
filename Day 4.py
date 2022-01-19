# 1. Update the first set with items that don’t exist in the second set.

# Given:
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# Expected output : {10, 30}

set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))

# 2. Return a set of elements present in set A or B, but not both.

# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output : {20, 70, 10, 60}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 ^ set2)

# 3.Remove items from set1 that are not common to both set1 and set2

# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output : {40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
