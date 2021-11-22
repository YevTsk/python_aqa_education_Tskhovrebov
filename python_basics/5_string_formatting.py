name = "John"
age = 23
my_list = [1, 2, 3]


print("Hello, %s!" % name)
print(f'Hello, {name}!')
print(f'{name} is {age} years old.')
print(f'A list {my_list}')

# Exercise

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
