

with open('input', 'r') as data_file:
    choices = list(data_file.readlines())
    valid_passwords = []


    for items in choices:
        items = items.split(' ')
        min_val, max_val = items[0].split('-')
        char = items[1].strip(':')
        password = items[2].strip('\n')
        min_val = int(min_val) -1
        max_val = int(max_val) -1





        # om char finnns på  EN AV plats min val eller max val i string, är det OK.
        # om char finns på plats min val XOR max val i password, then OK.
        if password[min_val] == char and password[max_val] == char:
            continue
        if password[min_val] == char or password[max_val] == char:
            valid_passwords.append(password)

    print(len(valid_passwords))

