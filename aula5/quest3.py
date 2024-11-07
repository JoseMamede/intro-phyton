#Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.
numb1 = int(input("Digite o primeiro número:"))
numb2 = int(input("Digite o segundo número:"))
operacao = input("Digite uma operação:(+, -, *, /)")

if operacao == "+":
    soma = numb1 + numb2
    print(f"A soma de {numb1} e {numb2} é: {soma}")
elif operacao == "-":
    subtracao = numb1 - numb2
    print(f"A subtração de {numb1} e {numb2} é: {subtracao}")
elif operacao == "*":
    multi = numb1 - numb2
    print(f"A multiplicação de {numb1} e {numb2} é: {multi}")
elif operacao == "/":
    if numb2 == 0:
        print("Não é possivel dividir por zero")
    divi = numb1 - numb2
    print(f"A Divisão de {numb1} e {numb2} é: {divi}")
