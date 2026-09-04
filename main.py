# Resolução 

valor = str(1250.5)
if valor[-2] == '.':
    valor += "0"

print(f"R$ {valor.replace('.', ',')}")

valor = str(0.857)

if valor[0] == "0":
    final =  "%"
    valor = (valor[2:] + final)
    metade = valor[0:2]

    resotado = metade + "," + valor[2:]

print(resotado)

# Resolução proposta

valor = (1250.5)

print(f'R$ {valor:.2f}'.replace('.', ',') )

valor = 0.857 

print(f'{valor:.2%}'.replace('.', ','))