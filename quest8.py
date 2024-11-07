#Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."
numero1 = int(input("digite um numero:"))
numero2 = int(input("digite um numero:"))
soma = numero1 + numero2
sub = numero1 - numero2
multi = numero1 * numero2
divisao = numero1 / numero2
print(f"""
    soma de numero1 e numero2 é {soma}
    subtração de numero1 e numero2 é {sub}
    multiplicação de numero1 e numero2 é {multi}
    divisão de numero1 e numero2 é {divisao} 
      """)