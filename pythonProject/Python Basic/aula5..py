"""
Aula 5 - Operadores Aritmédicos
"""


"""
+, -, /, //, *, **, (), % 
"""
print("Soma +: " , 10 + 10) #Soma de duas string resulta em contaneção EX:
print("Concatenação: " , '5'+'5')
print("Multiplicação *: " , 10 * 10) #Também serve como repetição EX:
print("Repetição com *: ", 10 * "Lucas")
print("Divisão /: " , 10 / 10)
print("Potênciação **: " , 10 ** 10)
print("Resto da divisão %:" , 10 % 10)
print("Subtração - : " , 10 - 10)
print("Divisão arredondada para baixo //: " , 10 // 3)
print(10 + 10 * 2)  #parênteses define a ordem da operação!
print((10 + 10)*2)

"""
( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

Observação: existem muito mais operadores do que estes em Python e todoseles também têm precedência,
 você pode ver a lista completa em 
https://docs.python.org/3/reference/expressions.html#operator-precedence 
(sempre utilize a documentação oficial como reforço caso necessário).
"""