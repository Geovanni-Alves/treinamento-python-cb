velocidade = 55
if velocidade <= 50:
    print("Nao foi multado")
elif velocidade >= 51 and velocidade <= 60:
    print("Levou multa de 2 pontos")
elif velocidade >= 61 and velocidade <= 75:
    print("Levou multa de 2 pontos")
else:
    print("Levou multa de 7 pontos")

# Chaining
if velocidade <= 50:
    print("Nao foi multado")
elif 51 <= velocidade <= 60:  # Chaining
    print("Levou multa de 2 pontos")
elif velocidade >= 61 and velocidade <= 75:
    print("Levou multa de 2 pontos")
else:
    print("Levou multa de 7 pontos")
