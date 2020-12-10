import re

data = [x.replace('\n', ' ').split(' ') for x in open('input').read().split('\n\n')]


def valid_passport(x):
    req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    present_fields = {f.split(':')[0] for f in x}

    return req_fields.issubset(present_fields)


def has_valid_data(x):
    field, value = x.split(':')
    field_pattern = {'byr': '(^(19)[2-9][0-9]$)|(^(200)[0-2]$)',
                     'iyr': '(^(201)[0-9]$)|(^(2020)$)',
                     'eyr': '(^(202)[0-9]$)|(^(2030)$)',
                     'hgt': '(^((1[5-8][0-9])|((19)[0-3]))cm$)|(^((59)|(6[0-9])|(7[0-6]))in$)',
                     'hcl': '^#[0-9a-f]{6}$',
                     'ecl': '(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)',
                     'pid': '^[0-9]{9}$',
                     'cid': '(.*?)'}

    return bool(re.match(field_pattern[field], value))


'''Den här kommentaren är bara för att testa om hur man mergar.'''


def extra_valid_passport(x):
    return valid_passport(x) and all(has_valid_data(p) for p in x)


def part_1():
    return sum([valid_passport(x) for x in data])


def part_2():
    return sum([extra_valid_passport(x) for x in data])


print(f'{part_1()} - {part_2()}')
