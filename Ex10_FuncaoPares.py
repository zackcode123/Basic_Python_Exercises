'''Escreva uma função que verifica se um número é par ou impar. '''

def numero(x):
     if x %2 == 0:
          print('Numero Par')
     else:
          print('Numero Impar')
           
x = int(input('Digite um numero: '))
numero(x)
