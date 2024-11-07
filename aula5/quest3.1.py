#mesma questão só que com match case ( ͡~ ͜ʖ ͡°)
numb1 = int(input("Digite o primeiro número:"))
numb2 = int(input("Digite o segundo número:"))
operacao = input("Digite uma operação:(+, -, *, /)")

match operacao:
    case "+":
        soma = numb1 + numb2
        print(f"A soma de {numb1} e {numb2} é: {soma}")
    case "-":
        subt = numb1 - numb2
        print(f"A subtração de {numb1} e {numb2} é: {subt}")
    case "*":
        mult = numb1 * numb2
        print(f"A multiplicação de {numb1} e {numb2} é: {mult}")
    case "/":
        if numb2 == 0:
            print("Não é possivel dividir por zero")
        divi = numb1 / numb2
        print(f"A divisão de {numb1} e {numb2} é: {divi}")