string = 'Hello world'

print(string.upper())
print(string.lower())
print(string.title())

print(string[0])
print(string[-1])
print(string[0:4])
print(string[5:])
print(string[::2])
print(string[::-1])
print(len(string))

string = ' Hello world '
print(string.strip())
print(string.capitalize())
print(string.strip().capitalize())

string_list = string.split()
print(string_list)
print('*'.join(string_list))
