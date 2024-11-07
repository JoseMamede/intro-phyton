#Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.
numb1 = int(input("Digite o primeiro número:"))
numb2 = int(input("Digite o segundo número:"))
numb3 = int(input("Digite o terceiro número:"))

if numb1 > numb2 and numb1 > numb3:
    print(f"O maior número dos três é: {numb1}")
elif numb2 > numb1 and numb2 > numb3:
    print(f"O maior número dos três é: {numb2}")
elif numb3 > numb1 and numb3 > numb2:
    print(f"O maior número dos três é: {numb3}")

