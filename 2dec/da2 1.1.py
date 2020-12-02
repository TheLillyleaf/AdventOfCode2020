from collections import Counter

with open('input', 'r') as data_file:
    choices = list(data_file.readlines())
    valid_passwords = []


    for items in choices:
        items = items.split(' ')
        min_val, max_val = items[0].split('-')
        char = items[1].strip(':')
        password = items[2].strip('\n')
        total_occurance = Counter(password)

        if int(min_val) <= int(total_occurance[char]) <= int(max_val):
            valid_passwords.append(password)



    print(len(valid_passwords))