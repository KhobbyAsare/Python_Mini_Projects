"""
for loop = execute a block of code a fixed number of times
            you can iterate over a range, string, sequence, list etc.

"""

for counter in range(1, 11):
    pass
    # print(counter)

print('HURRAYING...')

for counter in reversed(range(1, 11)):
    pass
    # print(counter)

# ....................

creditsCard_number = "1234-5676-2323-3454"

for num in creditsCard_number:
    print(num)

for counter in range(1, 21):
    if counter == 13:
        continue
    # print(counter)


for counter in range(1, 21):
    if counter == 13:
        break
    print(counter)