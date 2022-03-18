""" # conversao de tipos
idade = int(input("Qual e a sua idade?: "))
print(idade > 18)

altura_parede = input("Qual é a altura da parede? ")
print(float(altura_parede) > 2.10)

list()
tuple()
dict() """

idade = 18
print("Maior de idade") if idade >= 18 else print("Menor de idade")
# operador ternario (expressao if condicao else expressao)

possui_passaporte = True

print("Favor embarcar ") if possui_passaporte else print(
    "Favor Tirar Passaporte")
