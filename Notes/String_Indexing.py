"""
indexing = accessing elements of a sequence using [] (indexing operator)

            [start: end: step]
"""

credits_number = "1234-5678-9034-3456"

print(credits_number[3])
print(credits_number[5:])
print(credits_number[-1])  # last index
print(credits_number[1: 9])
print(credits_number[1: 14: 2])
print(credits_number[:: 2])

last_four_digits = credits_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_four_digits}")

reverse_creditCard_number = credits_number[::-1]
print(reverse_creditCard_number)
