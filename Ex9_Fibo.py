'''A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 
Escreva um programa que apresente a série de Fibonacci até o n-ésimo termo (n > 0).'''


while True:

    n = int(input("\nDigite o termo que queira descobrir na sequência Fibonacci: "))

    i = 0
    a = 0
    b = 1

    if n > 0:

        print("\n%dº termo: %d" % (b, b))
        i += 1
        a = b

        while i < n:

            print("\n%dº termo: %d" % (i+1, b))
            b = a + b
            i += 1
            a = b - a
        else:
            break
