from os import remove

calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(a):
    count_calls()
    return (len(a), a.upper(), a.lower())
def is_contains(string, list):
    count_calls()
    list_1 = []
    for i in list:
        a = i.lower()
        list_1.append(a)
    return (string.lower() in list_1)

print(string_info('PaVeL'))
print(string_info('AnaSTasiy'))
print(string_info('LizA'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)