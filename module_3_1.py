calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    string_ = (len(string), string.upper(), string.lower())
    count_calls()
    return string_

def is_contains(string, list_to_search):
    list = []
    for i in list_to_search:
        list.append(i.lower())
    string_ = (string.lower() in (list))
    count_calls()
    return string_


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
