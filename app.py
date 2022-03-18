import random

print(random.random())
print(random.uniform(4, 10))
print(random.randint(1, 60))

cores = ["vermelho", "azul", "preto", "amarelo"]

print(random.choices(cores, k=2))

cartas_baralho = ["Zap", "Copas", "2", "3",
                  "Espatilha", "Ouro", "K", "Q", "J", "A"]
print(random.shuffle(cartas_baralho))
print(cartas_baralho)
