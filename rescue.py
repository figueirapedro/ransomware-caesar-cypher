#   Ransomware para decriptografia
#
#   Desenvolvido por Pedro Figueira, Jean Alves, Vinicius Bonicio, Kathellin Ribeiro

f = open("notas.txt", "r")

texto = f.read()
f.close()

criptografado = ""

for caracter in texto:
    criptografado = criptografado + chr(ord(caracter) - 7)

f = open("notas.txt", "w")
f.write(criptografado)
f.close()

f = open("notas.txt", "r")
sequestrado = f.read()
f.close()

g = open("backup.txt", "r")
original = g.read()

if sequestrado == original:
    print("Texto resgatado com sucesso!")
else:
    print("Texto foi quebrado :(")