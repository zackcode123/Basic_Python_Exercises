'''Faça um programa que calcule o fatorial de um número inteiro e natural
   fornecido pelo usuário. 
   Exemplo: 5! = 5 x 4 x 3 x 2 x 1=120. (A saída deve exibida ser conforme o exemplo)
   Por definição 0! = 1.'''

num = int(input("Digite um Número para calculao seu Fatorial: "))
fat = 1
x = 1
i = num
temp = str(num)+"! = "
while x <= num:
    fat *= x
    x += 1
    i = i - 1
    if i > 1:
        temp = temp + str(i) + " x "
    elif i == 1:
        temp = temp + str(i)
print(temp + " = " + str(fat))
