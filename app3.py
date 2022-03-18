idade = 21
possui_convite = False
filho_do_dono = True
print((idade >= 21) and (possui_convite == True))
print((idade >= 21) or (possui_convite == True))
# maior de 21 ou possui convite ou seja filho do dono
print((idade >= 21) and (possui_convite == True) or (filho_do_dono == True))


maior_de_idade = True
possui_ctps = True
esta_trabalhando = True
possui_veiculo = False
print((maior_de_idade == True) and (possui_ctps == True))
print((maior_de_idade and possui_ctps))

print((not possui_veiculo) and (possui_ctps == True))
