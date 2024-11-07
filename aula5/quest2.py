#Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário um número e verifica se ele é par ou ímpar.
numb = int(input("Direi se seu número é par ou ímpar. Diga um número:"))
if numb % 2 == 0:
    print("Seu número é par.")
else:
    print("Seu número é ímpar.")