"""
Aula 9 - Entrada de dados (input)
"""
name = input('Whats your name? ')           #input sempre retorna string!
print(f'your name is {name}, and your type is ' f'{type(name)}.')
age = input("Whats your age? ")
print(f"{name} have {age} years old.")
yearsOfBirth = 2021 - int(age)
print(f'{name} he was born in {yearsOfBirth}')

"""
Mini calculadora
"""

num_1 = input("Whats a fisrt number? ")
num_2 = input("Whats a second number? ")
print(f'the sum of {num_1} and {num_2} results in: ',int(num_1)+ int(num_2))