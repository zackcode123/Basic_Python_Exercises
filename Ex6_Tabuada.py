'''1)(2.0 pontos)Desenvolva um gerador de tabuadas, capaz de gerar a tabuada de qualquer número
inteiro de valor_inicial até valor_final. O usuário deve informar o valor_inicial e o valor_final.
A saída deve ser conforme o exemplo abaixo:
Valor inicial = 3
Valor final = 6
Tabuada de 3
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
Tabuada de 4
...
Tabuada de 5
...
Tabuada de 6
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
Observação: o valor_inicial deve ser inferior ao valor_final e ambos devem ser inteiros e positivos.'''


print('TABUADA')
n=int(input('Informe o menor número positivo para início da tabuada: '))
n1=int(input('Informe o maior número positivo para encerramento da tabuada: '))
cont=n
while cont<=n1:
    for x in range(0, 11):
        print(cont, 'x', x, '=', cont*x)
    cont+=1