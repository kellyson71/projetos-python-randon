turno = input("Digite M para matutino, V para vespertino, ou N para noturno: ")

if turno.upper() == 'M':
    print("Bom Dia!")
elif turno.upper() == 'V':
    print("Boa Tarde!")
elif turno.upper() == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
