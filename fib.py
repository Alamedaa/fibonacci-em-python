"""
Sequência de Fibonacci é a sequência numérica proposta pelo matemático Leonardo Pisa
Entendendo o fibonacci:
Serie de fibonacci comeca com 0 e 1
A = 0
b = 1
a  b
0  1
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
Assim, começando pelo 1, essa sequência é formada somando cada numeral com o numeral que o antecede
No caso do 1, repete-se esse numeral e soma-se, ou seja, 1 + 1 = 2.
"""
def fibonacci(tam):
    a , b = 0 , 1
    while a < tam:
	a , b = b , b + a
	print(a, end = " ")
    print()
