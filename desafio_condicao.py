possui_passaporte = True
passagem_comprada = True
menor_de_idade = False

print((possui_passaporte and passagem_comprada) and not menor_de_idade)
print((not possui_passaporte and passagem_comprada) and not menor_de_idade)
print((not possui_passaporte and not passagem_comprada) and menor_de_idade)
print((not possui_passaporte and not passagem_comprada) and menor_de_idade)
