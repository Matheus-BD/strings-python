valor = str(1250.5)
if valor[-2] == '.':
    valor += "0"

print(f"R$ {valor.replace('.', ',')}")



valor = 0.857

print(f"{valor:.2%}".replace(".", ","))