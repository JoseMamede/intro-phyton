#Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
lado1 = int(input("Digite o primeiro lado do triângulo:"))
lado2 = int(input("Digite o segundo lado do triângulo:"))
lado3 = int(input("Digite o terceiro lado do triângulo:"))

if lado1 == lado2 and lado1 == lado3:
    print("O triângulo é equilátero")
elif lado1 == lado2 or lado3 == lado1 or lado2 == lado3:
    print("O triângulo é isósceles")
elif lado1 == lado2 or lado3 == lado1 or lado2 == lado3:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
    
