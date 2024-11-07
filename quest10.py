#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."
name = input("Digite seu nome:")
partes = name.split(sep=" ")
print(f"{partes[0][0]}.{partes[1][0]}.{partes[2][0]}")
