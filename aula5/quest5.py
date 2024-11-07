#Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
age = int(input("Digite sua idade:"))

if age >= 0 and age >= 12:
    print("Criança")
elif age >= 13 and age >= 19:
    print("Adolescente")
elif age >= 20 and age >= 59:
    print("Adulto")
elif age >= 60 and age >= 70:
    print("Idoso")
else:
    print("idade invalida")



