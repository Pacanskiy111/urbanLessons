from operator import contains

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    string = tuple([len(string), string.upper(), string.lower()])
    return string

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [char.lower() for char in list_to_search]
    if string in list_to_search:
        in_list = True
    else:
        in_list = False
    return in_list

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)