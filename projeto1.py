from datetime import datetime
import random
# Modulo 1 - Gerar registro do funcionario
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
data_nascimento = datetime.strptime(
    input("Digite a data de aniversario: "), "%d/%m/%Y")
cartoes = ["R$ 50,00", "R$ 250,00", "R$ 120,00"]
data_cadastro_dia = datetime.now().day
data_cadastro_mes = datetime.now().month
data_cadastro_ano = datetime.now().year

cartao_sorteado = random.choice(cartoes)


# Modulo 2 - Gerar apresentação para o usuario
print(f"Ola {nome}, seu registro foi concluido com sucesso "
      f"no dia {data_cadastro_dia}/{data_cadastro_mes}/{data_cadastro_ano} Parabens, \n "
      f"houve um sorteio e voce ganhou um cartao de compras no valor de {cartao_sorteado}.")
